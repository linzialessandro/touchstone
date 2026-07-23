"""Deterministic grading: write candidate code, run task tests in a subprocess."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from code_reason.models import Attempt, Grade, GradeStatus, Task


def grade_attempt(task: Task, attempt: Attempt) -> Grade:
    if attempt.error:
        return Grade(
            attempt_id=attempt.id,
            task_id=task.id,
            status=GradeStatus.ERROR,
            score=0.0,
            message=f"attempt error: {attempt.error}",
        )

    code = attempt.extracted_code
    if not code or not code.strip():
        return Grade(
            attempt_id=attempt.id,
            task_id=task.id,
            status=GradeStatus.FAIL,
            score=0.0,
            message="no code extracted from response",
        )

    task_dir = task.task_dir()
    try:
        with tempfile.TemporaryDirectory(prefix=f"cr-{task.id}-") as tmp:
            tmp_path = Path(tmp)
            solution = tmp_path / "solution.py"
            solution.write_text(code, encoding="utf-8")

            # Copy test modules next to solution so imports stay simple.
            for rel in task.test_files:
                src = task_dir / rel
                if not src.exists():
                    return Grade(
                        attempt_id=attempt.id,
                        task_id=task.id,
                        status=GradeStatus.ERROR,
                        score=0.0,
                        message=f"missing test file: {rel}",
                    )
                dest = tmp_path / Path(rel).name
                dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

            # Run each test file as a script with solution on PYTHONPATH cwd.
            combined_stdout: list[str] = []
            combined_stderr: list[str] = []
            for rel in task.test_files:
                test_name = Path(rel).name
                proc = subprocess.run(
                    [sys.executable, test_name],
                    cwd=tmp_path,
                    capture_output=True,
                    text=True,
                    timeout=task.timeout_seconds,
                    check=False,
                )
                combined_stdout.append(proc.stdout)
                combined_stderr.append(proc.stderr)
                if proc.returncode != 0:
                    return Grade(
                        attempt_id=attempt.id,
                        task_id=task.id,
                        status=GradeStatus.FAIL,
                        score=0.0,
                        message=f"tests failed ({test_name}) exit={proc.returncode}",
                        details={
                            "stdout": "\n".join(combined_stdout)[-4000:],
                            "stderr": "\n".join(combined_stderr)[-4000:],
                        },
                    )

            return Grade(
                attempt_id=attempt.id,
                task_id=task.id,
                status=GradeStatus.PASS,
                score=1.0,
                message="all tests passed",
                details={
                    "stdout": "\n".join(combined_stdout)[-2000:],
                },
            )
    except subprocess.TimeoutExpired:
        return Grade(
            attempt_id=attempt.id,
            task_id=task.id,
            status=GradeStatus.ERROR,
            score=0.0,
            message=f"timeout after {task.timeout_seconds}s",
        )
    except OSError as exc:
        return Grade(
            attempt_id=attempt.id,
            task_id=task.id,
            status=GradeStatus.ERROR,
            score=0.0,
            message=f"grader os error: {exc}",
        )
