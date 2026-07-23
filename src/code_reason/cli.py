"""CLI: list tasks, grade a solution file, run open-model / mock evals."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from code_reason import __version__
from code_reason.extract import extract_python_code
from code_reason.grader import grade_attempt
from code_reason.loader import DEFAULT_TASKS_DIR, REPO_ROOT, discover_tasks, get_task
from code_reason.models import Attempt
from code_reason.providers import get_provider
from code_reason.runner import run_eval, save_run

app = typer.Typer(
    name="code-reason",
    help="Touchstone — coding-reasoning eval for open-weight models (Grok designs; does not compete).",
    add_completion=False,
    no_args_is_help=True,
)
console = Console()


@app.command("version")
def version() -> None:
    console.print(f"code-reason {__version__}")


@app.command("list-tasks")
def list_tasks(
    tasks_dir: Optional[Path] = typer.Option(None, help="Override tasks directory"),
) -> None:
    tasks = discover_tasks(tasks_dir)
    if not tasks:
        console.print(f"[yellow]No tasks found in {tasks_dir or DEFAULT_TASKS_DIR}[/yellow]")
        raise typer.Exit(1)

    table = Table(title="Tasks")
    table.add_column("id")
    table.add_column("title")
    table.add_column("provenance")
    table.add_column("tags")
    for t in tasks:
        table.add_row(t.id, t.title, t.provenance.value, ", ".join(t.tags))
    console.print(table)


@app.command("grade-file")
def grade_file(
    task_id: str = typer.Argument(..., help="Task id"),
    solution: Path = typer.Argument(..., exists=True, readable=True, help="Python solution file"),
    tasks_dir: Optional[Path] = typer.Option(None),
) -> None:
    """Grade a local solution without calling a model (ownership drills)."""
    task = get_task(task_id, tasks_dir)
    code = solution.read_text(encoding="utf-8")
    attempt = Attempt(
        task_id=task.id,
        provider="local",
        model="file",
        prompt=task.prompt,
        raw_response=code,
        extracted_code=extract_python_code(code),
    )
    grade = grade_attempt(task, attempt)
    color = "green" if grade.status.value == "pass" else "red"
    console.print(f"[{color}]{grade.status.value}[/{color}] score={grade.score} — {grade.message}")
    if grade.details.get("stderr"):
        console.print(grade.details["stderr"])
    raise typer.Exit(0 if grade.status.value == "pass" else 1)


@app.command("run")
def run_cmd(
    provider: str = typer.Option(
        None,
        "--provider",
        "-p",
        help="mock | hf (default: env CODE_REASON_PROVIDER or mock)",
    ),
    model: str = typer.Option(
        None,
        "--model",
        "-m",
        help="HF model id for provider=hf (default: env CODE_REASON_MODEL)",
    ),
    task: Optional[list[str]] = typer.Option(
        None,
        "--task",
        "-t",
        help="Task id (repeatable). Default: all tasks.",
    ),
    tasks_dir: Optional[Path] = typer.Option(None),
    out_dir: Path = typer.Option(REPO_ROOT / "runs", "--out"),
) -> None:
    """Run the eval and write a JSON run artifact (open models / mock only)."""
    prov = get_provider(provider)
    if prov.name == "mock":
        model_name = model or os.environ.get("CODE_REASON_MODEL") or "mock-golden"
    else:
        model_name = (
            model
            or os.environ.get("CODE_REASON_MODEL")
            or "Qwen/Qwen2.5-1.5B-Instruct"
        )

    console.print(f"Provider={prov.name} model={model_name}")
    run = run_eval(prov, model_name, task_ids=task, tasks_dir=tasks_dir)
    path = save_run(run, out_dir)

    table = Table(title="Results")
    table.add_column("task")
    table.add_column("status")
    table.add_column("score")
    table.add_column("message")
    for g in run.grades:
        table.add_row(g.task_id, g.status.value, f"{g.score:.1f}", g.message)
    console.print(table)

    s = run.summary
    rate = f"{s.pass_rate:.0%}" if s.pass_rate is not None else "n/a"
    console.print(
        f"pass={s.n_pass} fail={s.n_fail} error={s.n_error} skip={s.n_skip} pass_rate={rate}"
    )
    console.print(f"Wrote {path}")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()
