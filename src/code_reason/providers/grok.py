"""xAI Grok provider — frontier competitor (Grok 4.5).

Same harness and metric as open models. Used to enter Grok 4.5 into Touchstone
so it can compete (and possibly win) fairly. Requires XAI_API_KEY.
Not for Kaggle free-GPU participant notebooks (closed API).
"""

from __future__ import annotations

import os
import time

import httpx

from code_reason.providers.base import CompletionResult, Provider

DEFAULT_BASE = "https://api.x.ai/v1"
DEFAULT_MODEL = "grok-4.5"


class GrokProvider(Provider):
    name = "grok"

    def __init__(self, api_key: str | None = None, base_url: str | None = None) -> None:
        self.api_key = api_key or os.environ.get("XAI_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "XAI_API_KEY is not set. Needed to score Grok 4.5 as a Touchstone competitor."
            )
        self.base_url = (base_url or os.environ.get("XAI_BASE_URL") or DEFAULT_BASE).rstrip("/")

    def complete(self, prompt: str, *, model: str, system: str | None = None) -> CompletionResult:
        model = model or os.environ.get("CODE_REASON_MODEL") or DEFAULT_MODEL
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        t0 = time.perf_counter()
        with httpx.Client(timeout=180.0) as client:
            resp = client.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": messages,
                    "temperature": 0.0,
                },
            )
            resp.raise_for_status()
            data = resp.json()
        ms = (time.perf_counter() - t0) * 1000
        text = data["choices"][0]["message"]["content"]
        return CompletionResult(text=text, latency_ms=ms, raw=data)
