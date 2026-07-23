"""Core eval object model: Task, Attempt, Grade, Run.

Own these types. Everything else is glue.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class ProvenanceKind(str, Enum):
    ORIGINAL = "original"
    TRANSFORM = "transform"
    SYNTHETIC_FILTERED = "synthetic_filtered"


class Task(BaseModel):
    """A single code-reasoning item with an executable grade path."""

    id: str
    title: str
    prompt: str
    language: str = "python"
    # Relative to task directory; grader runs these.
    test_files: list[str] = Field(default_factory=lambda: ["tests.py"])
    timeout_seconds: float = 5.0
    provenance: ProvenanceKind = ProvenanceKind.ORIGINAL
    lineage_notes: str = ""
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    # Absolute path to the task folder (set when loaded).
    root: Path | None = None

    def task_dir(self) -> Path:
        if self.root is None:
            raise ValueError(f"Task {self.id} has no root path")
        return self.root


class Attempt(BaseModel):
    """One model (or human) response to a task."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    task_id: str
    provider: str
    model: str
    prompt: str
    raw_response: str
    extracted_code: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    latency_ms: float | None = None
    error: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class GradeStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    SKIP = "skip"


class Grade(BaseModel):
    """Deterministic (or explicitly non-deterministic) judgment of an attempt."""

    attempt_id: str
    task_id: str
    status: GradeStatus
    score: float = 0.0  # 1.0 pass, 0.0 fail for v0.1 binary tasks
    message: str = ""
    details: dict[str, Any] = Field(default_factory=dict)
    graded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RunSummary(BaseModel):
    n_tasks: int = 0
    n_pass: int = 0
    n_fail: int = 0
    n_error: int = 0
    n_skip: int = 0
    pass_rate: float | None = None


class Run(BaseModel):
    """A batch evaluation: attempts + grades + summary."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    provider: str
    model: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    task_ids: list[str] = Field(default_factory=list)
    attempts: list[Attempt] = Field(default_factory=list)
    grades: list[Grade] = Field(default_factory=list)
    summary: RunSummary = Field(default_factory=RunSummary)
    notes: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)

    def recompute_summary(self) -> None:
        s = RunSummary(n_tasks=len(self.grades))
        for g in self.grades:
            if g.status == GradeStatus.PASS:
                s.n_pass += 1
            elif g.status == GradeStatus.FAIL:
                s.n_fail += 1
            elif g.status == GradeStatus.ERROR:
                s.n_error += 1
            else:
                s.n_skip += 1
        scored = s.n_pass + s.n_fail
        s.pass_rate = (s.n_pass / scored) if scored else None
        self.summary = s
