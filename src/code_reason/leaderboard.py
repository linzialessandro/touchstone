"""Aggregate run JSON artifacts into a Touchstone leaderboard (open models only)."""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from code_reason.models import GradeStatus, Run


@dataclass
class LeaderboardRow:
    track: str
    display: str
    provider: str
    model: str
    n_tasks: int
    n_pass: int
    n_fail: int
    n_error: int
    pass_rate: float | None
    run_path: str
    by_tag: dict[str, float]


def _infer_track(provider: str, model: str) -> str:
    if provider == "mock":
        return "plumbing"
    return "open"


def load_runs(runs_dir: Path) -> list[tuple[Path, Run]]:
    out: list[tuple[Path, Run]] = []
    if not runs_dir.exists():
        return out
    for path in sorted(runs_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            out.append((path, Run.model_validate(data)))
        except (OSError, json.JSONDecodeError, ValueError):
            continue
    return out


def build_rows(
    runs_dir: Path,
    *,
    task_tags: dict[str, list[str]] | None = None,
    include_plumbing: bool = False,
) -> list[LeaderboardRow]:
    task_tags = task_tags or {}
    best: dict[tuple[str, str], LeaderboardRow] = {}

    for path, run in load_runs(runs_dir):
        if run.provider == "mock" and not include_plumbing:
            continue
        # Official LB: open-weight only
        if run.provider != "hf" and not (run.provider == "mock" and include_plumbing):
            continue

        s = run.summary
        rate = s.pass_rate
        if rate is None and (s.n_pass + s.n_fail) > 0:
            rate = s.n_pass / (s.n_pass + s.n_fail)

        by_tag_scores: dict[str, list[float]] = defaultdict(list)
        for g in run.grades:
            tags = task_tags.get(g.task_id, ["untagged"])
            score = 1.0 if g.status == GradeStatus.PASS else 0.0
            for tag in tags:
                by_tag_scores[tag].append(score)
        by_tag = {
            tag: (sum(v) / len(v) if v else 0.0) for tag, v in sorted(by_tag_scores.items())
        }

        row = LeaderboardRow(
            track=_infer_track(run.provider, run.model),
            display=run.model,
            provider=run.provider,
            model=run.model,
            n_tasks=s.n_tasks,
            n_pass=s.n_pass,
            n_fail=s.n_fail,
            n_error=s.n_error,
            pass_rate=rate,
            run_path=str(path),
            by_tag=by_tag,
        )
        key = (run.provider, run.model)
        prev = best.get(key)

        def _rank(r: LeaderboardRow) -> tuple[float, int]:
            return (r.pass_rate if r.pass_rate is not None else -1.0, r.n_tasks)

        if prev is None or _rank(row) > _rank(prev):
            best[key] = row

    rows = list(best.values())
    rows.sort(key=lambda r: (-(r.pass_rate or -1.0), r.model))
    return rows


def rows_to_markdown(rows: list[LeaderboardRow], *, title: str = "Touchstone Leaderboard") -> str:
    lines = [
        f"# {title}",
        "",
        "Metric: **pass rate** (executable unit tests).",
        "",
        "**Competitors:** open-weight models only.",
        "**Grok:** benchmark **designer** — not a leaderboard entry.",
        "",
        "| Rank | Model | Pass rate | Pass | Fail | Error | N |",
        "|------|-------|-----------|------|------|-------|---|",
    ]
    for i, r in enumerate(rows, start=1):
        rate = f"{r.pass_rate:.1%}" if r.pass_rate is not None else "n/a"
        lines.append(
            f"| {i} | `{r.display}` | {rate} | {r.n_pass} | {r.n_fail} | {r.n_error} | {r.n_tasks} |"
        )
    if not rows:
        lines.append("| — | *no open-model runs yet* | — | — | — | — | — |")
    lines.append("")
    lines.append("## Integrity")
    lines.append("")
    lines.append(
        "Open models only. Same harness and tests for all. "
        "Designer credit for Grok is separate from competition scores."
    )
    lines.append("")
    return "\n".join(lines)


def rows_to_csv(rows: list[LeaderboardRow]) -> str:
    header = "rank,track,provider,model,pass_rate,n_pass,n_fail,n_error,n_tasks,run_path"
    lines = [header]
    for i, r in enumerate(rows, start=1):
        rate = "" if r.pass_rate is None else f"{r.pass_rate:.6f}"
        lines.append(
            f"{i},{r.track},{r.provider},{r.model},{rate},{r.n_pass},{r.n_fail},{r.n_error},{r.n_tasks},{r.run_path}"
        )
    return "\n".join(lines) + "\n"
