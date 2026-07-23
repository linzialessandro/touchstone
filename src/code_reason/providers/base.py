"""Model provider interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CompletionResult:
    text: str
    latency_ms: float
    raw: dict | None = None


class Provider(ABC):
    name: str

    @abstractmethod
    def complete(self, prompt: str, *, model: str, system: str | None = None) -> CompletionResult:
        raise NotImplementedError
