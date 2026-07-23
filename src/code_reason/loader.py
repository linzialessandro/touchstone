"""Load tasks from the tasks/ directory."""

from __future__ import annotations

import json
from pathlib import Path

from code_reason.models import ProvenanceKind, Task

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TASKS_DIR = REPO_ROOT / "tasks" / "v0_1"


def load_task(task_dir: Path) -> Task:
    meta_path = task_dir / "task.json"
    if not meta_path.exists():
        raise FileNotFoundError(f"Missing task.json in {task_dir}")

    data = json.loads(meta_path.read_text(encoding="utf-8"))
    prompt_path = task_dir / data.get("prompt_file", "prompt.md")
    if not prompt_path.exists():
        raise FileNotFoundError(f"Missing prompt file: {prompt_path}")

    prompt = prompt_path.read_text(encoding="utf-8").strip()
    provenance = ProvenanceKind(data.get("provenance", "original"))

    return Task(
        id=data["id"],
        title=data.get("title", data["id"]),
        prompt=prompt,
        language=data.get("language", "python"),
        test_files=data.get("test_files", ["tests.py"]),
        timeout_seconds=float(data.get("timeout_seconds", 5.0)),
        provenance=provenance,
        lineage_notes=data.get("lineage_notes", ""),
        tags=data.get("tags", []),
        metadata=data.get("metadata", {}),
        root=task_dir.resolve(),
    )


def discover_tasks(tasks_dir: Path | None = None) -> list[Task]:
    root = tasks_dir or DEFAULT_TASKS_DIR
    if not root.exists():
        return []

    tasks: list[Task] = []
    for child in sorted(root.iterdir()):
        if child.is_dir() and (child / "task.json").exists():
            tasks.append(load_task(child))
    return tasks


def get_task(task_id: str, tasks_dir: Path | None = None) -> Task:
    for task in discover_tasks(tasks_dir):
        if task.id == task_id:
            return task
    raise KeyError(f"Unknown task id: {task_id}")
