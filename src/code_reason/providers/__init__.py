"""Provider factory.

  - mock — local plumbing (gold references)
  - hf   — open-weight competitors (prefer Kaggle GPU)

Grok is the benchmark designer, not a competitive provider.
"""

from __future__ import annotations

import os

from code_reason.providers.base import Provider
from code_reason.providers.hf import HuggingFaceProvider
from code_reason.providers.mock import MockProvider


def get_provider(name: str | None = None) -> Provider:
    name = (name or os.environ.get("CODE_REASON_PROVIDER") or "mock").lower()
    if name == "mock":
        mode = os.environ.get("CODE_REASON_MOCK_MODE", "golden")
        return MockProvider(mode=mode)
    if name in ("hf", "huggingface", "transformers"):
        return HuggingFaceProvider()
    if name == "grok":
        raise ValueError(
            "Grok is not a Touchstone competitor. "
            "Grok's role is benchmark design; only open-weight models (provider=hf) compete. "
            "Use mock | hf."
        )
    raise ValueError(f"Unknown provider: {name!r}. Use mock | hf")
