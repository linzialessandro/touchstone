#!/usr/bin/env python3
"""Validate every task: reference must pass; empty solution must fail.

Usage (from repo root, venv active):

    python scripts/validate_suite.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from code_reason.grader import grade_attempt  # noqa: E402
from code_reason.loader import discover_tasks  # noqa: E402
from code_reason.models import Attempt, GradeStatus  # noqa: E402


def main() -> int:
    tasks = discover_tasks()
    if not tasks:
        print("No tasks found.", file=sys.stderr)
        return 1

    failed = 0
    for task in tasks:
        ref_path = task.task_dir() / "reference.py"
        if not ref_path.exists():
            print(f"FAIL  {task.id}: missing reference.py")
            failed += 1
            continue

        ref_code = ref_path.read_text(encoding="utf-8")
        ok = grade_attempt(
            task,
            Attempt(
                task_id=task.id,
                provider="local",
                model="reference",
                prompt=task.prompt,
                raw_response=ref_code,
                extracted_code=ref_code,
            ),
        )
        empty = grade_attempt(
            task,
            Attempt(
                task_id=task.id,
                provider="local",
                model="empty",
                prompt=task.prompt,
                raw_response="",
                extracted_code="",
            ),
        )

        if ok.status != GradeStatus.PASS:
            print(f"FAIL  {task.id}: reference did not pass — {ok.message}")
            failed += 1
        elif empty.status == GradeStatus.PASS:
            print(f"FAIL  {task.id}: empty solution incorrectly passed")
            failed += 1
        else:
            print(f"OK    {task.id}")

    print(f"\n{len(tasks) - failed}/{len(tasks)} tasks OK")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
