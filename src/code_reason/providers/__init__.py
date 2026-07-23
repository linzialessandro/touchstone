"""Provider factory."""

from __future__ import annotations

import os

from code_reason.providers.base import Provider
from code_reason.providers.gemini import GeminiProvider
from code_reason.providers.grok import GrokProvider
from code_reason.providers.mock import MockProvider


def get_provider(name: str | None = None) -> Provider:
    name = (name or os.environ.get("CODE_REASON_PROVIDER") or "mock").lower()
    if name == "mock":
        mode = os.environ.get("CODE_REASON_MOCK_MODE", "golden")
        return MockProvider(mode=mode)
    if name == "grok":
        return GrokProvider()
    if name == "gemini":
        return GeminiProvider()
    raise ValueError(f"Unknown provider: {name}. Use mock | grok | gemini")
