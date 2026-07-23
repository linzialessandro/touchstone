"""Google Gemini generateContent API."""

from __future__ import annotations

import os
import time

import httpx

from code_reason.providers.base import CompletionResult, Provider

DEFAULT_MODEL = "gemini-2.0-flash"


class GeminiProvider(Provider):
    name = "gemini"

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY is not set")

    def complete(self, prompt: str, *, model: str, system: str | None = None) -> CompletionResult:
        model = model or os.environ.get("CODE_REASON_MODEL") or DEFAULT_MODEL
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent"
        )
        full_prompt = prompt if not system else f"{system}\n\n{prompt}"
        body = {
            "contents": [{"role": "user", "parts": [{"text": full_prompt}]}],
            "generationConfig": {"temperature": 0.0},
        }

        t0 = time.perf_counter()
        with httpx.Client(timeout=120.0) as client:
            resp = client.post(url, params={"key": self.api_key}, json=body)
            resp.raise_for_status()
            data = resp.json()
        ms = (time.perf_counter() - t0) * 1000

        try:
            text = data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"unexpected Gemini response: {data}") from exc
        return CompletionResult(text=text, latency_ms=ms, raw=data)
