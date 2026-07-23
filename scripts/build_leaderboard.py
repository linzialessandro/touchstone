#!/usr/bin/env python3
"""Build Markdown + CSV leaderboard from runs/*.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from code_reason.leaderboard import build_rows, rows_to_csv, rows_to_markdown  # noqa: E402
from code_reason.loader import discover_tasks  # noqa: E402


def main() -> int:
    runs_dir = REPO / "runs"
    out_dir = REPO / "leaderboard"
    out_dir.mkdir(parents=True, exist_ok=True)

    tags = {t.id: t.tags for t in discover_tasks()}
    rows = build_rows(runs_dir, task_tags=tags)
    if not rows:
        print(
            "No open-model runs in runs/ yet (mock/plumbing excluded from official LB).\n"
            "Run: python scripts/run_baselines.py --track open --only <HF_MODEL_ID>",
            file=sys.stderr,
        )

    md = rows_to_markdown(rows)
    csv = rows_to_csv(rows)
    (out_dir / "LEADERBOARD.md").write_text(md, encoding="utf-8")
    (out_dir / "leaderboard.csv").write_text(csv, encoding="utf-8")
    (out_dir / "leaderboard.json").write_text(
        json.dumps(
            [
                {
                    "track": r.track,
                    "provider": r.provider,
                    "model": r.model,
                    "pass_rate": r.pass_rate,
                    "n_pass": r.n_pass,
                    "n_fail": r.n_fail,
                    "n_error": r.n_error,
                    "n_tasks": r.n_tasks,
                    "by_tag": r.by_tag,
                    "run_path": r.run_path,
                }
                for r in rows
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(md)
    print(f"Wrote {out_dir / 'LEADERBOARD.md'}")
    print(f"Wrote {out_dir / 'leaderboard.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
