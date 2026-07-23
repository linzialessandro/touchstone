from pathlib import Path

from code_reason.extract import extract_python_code
from code_reason.grader import grade_attempt
from code_reason.loader import discover_tasks
from code_reason.models import Attempt, GradeStatus
from code_reason.providers.mock import MockProvider
from code_reason.runner import run_eval


def test_discover_three_tasks() -> None:
    tasks = discover_tasks()
    ids = {t.id for t in tasks}
    assert "001_sliding_window_max" in ids
    assert "002_parse_ini_sections" in ids
    assert "003_race_condition_fix" in ids


def test_references_pass() -> None:
    for task in discover_tasks():
        ref = task.task_dir() / "reference.py"
        code = ref.read_text(encoding="utf-8")
        attempt = Attempt(
            task_id=task.id,
            provider="local",
            model="reference",
            prompt=task.prompt,
            raw_response=code,
            extracted_code=code,
        )
        grade = grade_attempt(task, attempt)
        assert grade.status == GradeStatus.PASS, (task.id, grade.message, grade.details)


def test_empty_code_fails() -> None:
    task = next(t for t in discover_tasks() if t.id == "001_sliding_window_max")
    attempt = Attempt(
        task_id=task.id,
        provider="local",
        model="empty",
        prompt=task.prompt,
        raw_response="",
        extracted_code="",
    )
    grade = grade_attempt(task, attempt)
    assert grade.status == GradeStatus.FAIL


def test_extract_fence() -> None:
    text = "Sure!\n```python\nprint(1)\n```\n"
    assert extract_python_code(text) == "print(1)"


def test_mock_run_all_pass() -> None:
    run = run_eval(MockProvider(mode="golden"), "mock-golden")
    assert run.summary.n_pass == run.summary.n_tasks
    assert run.summary.n_fail == 0
