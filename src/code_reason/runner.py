"""Run tasks against a provider and grade attempts."""

from __future__ import annotations

import json
from pathlib import Path

from code_reason.extract import extract_python_code
from code_reason.grader import grade_attempt
from code_reason.loader import discover_tasks
from code_reason.models import Attempt, Run, Task
from code_reason.providers.base import Provider

SYSTEM = (
    "You are solving a code-reasoning evaluation task. "
    "Return a complete solution in a single Python markdown fence. "
    "Do not omit functions required by the prompt. "
    "No explanations outside the fence are required."
)


def build_user_prompt(task: Task) -> str:
    return f"TASK_ID: {task.id}\n\n{task.prompt}"


def run_eval(
    provider: Provider,
    model: str,
    *,
    task_ids: list[str] | None = None,
    tasks_dir: Path | None = None,
) -> Run:
    tasks = discover_tasks(tasks_dir)
    if task_ids:
        wanted = set(task_ids)
        tasks = [t for t in tasks if t.id in wanted]
        missing = wanted - {t.id for t in tasks}
        if missing:
            raise KeyError(f"Unknown task ids: {sorted(missing)}")

    run = Run(provider=provider.name, model=model)
    for task in tasks:
        run.task_ids.append(task.id)
        user_prompt = build_user_prompt(task)
        try:
            result = provider.complete(user_prompt, model=model, system=SYSTEM)
            code = extract_python_code(result.text)
            attempt = Attempt(
                task_id=task.id,
                provider=provider.name,
                model=model,
                prompt=user_prompt,
                raw_response=result.text,
                extracted_code=code,
                latency_ms=result.latency_ms,
            )
        except Exception as exc:  # noqa: BLE001 — record and continue
            attempt = Attempt(
                task_id=task.id,
                provider=provider.name,
                model=model,
                prompt=user_prompt,
                raw_response="",
                extracted_code=None,
                error=str(exc),
            )
        grade = grade_attempt(task, attempt)
        run.attempts.append(attempt)
        run.grades.append(grade)

    run.recompute_summary()
    return run


def save_run(run: Run, runs_dir: Path) -> Path:
    runs_dir.mkdir(parents=True, exist_ok=True)
    stamp = run.created_at.strftime("%Y%m%dT%H%M%SZ")
    path = runs_dir / f"{stamp}_{run.provider}_{run.model}_{run.id[:8]}.json"
    path.write_text(run.model_dump_json(indent=2), encoding="utf-8")
    return path


def load_run(path: Path) -> Run:
    return Run.model_validate(json.loads(path.read_text(encoding="utf-8")))
