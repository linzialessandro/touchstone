"""Hugging Face Transformers provider for open-weight models.

Designed for local GPUs and Kaggle notebooks. Optional dependency:

    pip install -e ".[oss]"

Open-weight competitors only (no closed APIs on the competitive path).
"""

from __future__ import annotations

import os
import time
from typing import Any

from code_reason.providers.base import CompletionResult, Provider

DEFAULT_MODEL = "Qwen/Qwen2.5-1.5B-Instruct"


class HuggingFaceProvider(Provider):
    """Generate code completions with a local (or Kaggle) HF causal LM."""

    name = "hf"

    def __init__(
        self,
        model_id: str | None = None,
        *,
        device_map: str | None = None,
        max_new_tokens: int | None = None,
        temperature: float | None = None,
    ) -> None:
        self.model_id = model_id or os.environ.get("CODE_REASON_MODEL") or DEFAULT_MODEL
        self.device_map = device_map or os.environ.get("CODE_REASON_DEVICE_MAP") or "auto"
        self.max_new_tokens = int(
            max_new_tokens
            if max_new_tokens is not None
            else os.environ.get("CODE_REASON_MAX_NEW_TOKENS", "1024")
        )
        self.temperature = float(
            temperature
            if temperature is not None
            else os.environ.get("CODE_REASON_TEMPERATURE", "0.0")
        )
        self._pipe: Any | None = None

    def _ensure_pipeline(self) -> Any:
        if self._pipe is not None:
            return self._pipe
        try:
            import torch
            from transformers import pipeline
        except ImportError as exc:
            raise RuntimeError(
                "Hugging Face provider requires optional deps. "
                'Install with: pip install -e ".[oss]"'
            ) from exc

        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self._pipe = pipeline(
            "text-generation",
            model=self.model_id,
            device_map=self.device_map,
            torch_dtype=dtype,
            trust_remote_code=os.environ.get("CODE_REASON_TRUST_REMOTE_CODE", "0") == "1",
        )
        return self._pipe

    def complete(self, prompt: str, *, model: str, system: str | None = None) -> CompletionResult:
        # Allow per-call model override by rebuilding if changed.
        if model and model not in ("default", "mock-golden") and model != self.model_id:
            self.model_id = model
            self._pipe = None

        pipe = self._ensure_pipeline()
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        gen_kwargs: dict[str, Any] = {
            "max_new_tokens": self.max_new_tokens,
            "do_sample": self.temperature > 0,
            "return_full_text": False,
        }
        if self.temperature > 0:
            gen_kwargs["temperature"] = self.temperature

        t0 = time.perf_counter()
        # Prefer chat template when the tokenizer supports it.
        tokenizer = getattr(pipe, "tokenizer", None)
        if tokenizer is not None and getattr(tokenizer, "chat_template", None):
            text_in = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
            outputs = pipe(text_in, **gen_kwargs)
            text = outputs[0]["generated_text"]
        else:
            flat = (system + "\n\n" if system else "") + prompt
            outputs = pipe(flat, **gen_kwargs)
            text = outputs[0]["generated_text"]
        ms = (time.perf_counter() - t0) * 1000
        return CompletionResult(
            text=text,
            latency_ms=ms,
            raw={"model": self.model_id, "provider": "hf"},
        )
