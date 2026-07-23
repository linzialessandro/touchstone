#!/usr/bin/env python3
"""Export a *public* task package (no reference solutions).

Use this for Kaggle datasets / competition public data.

    python scripts/export_public_tasks.py
    python scripts/export_public_tasks.py --out dist/kaggle_public
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "tasks" / "v0_1"
PUBLIC_FILES = ("task.json", "prompt.md", "tests.py")


def export(out: Path) -> int:
    if not SRC.exists():
        raise SystemExit(f"missing {SRC}")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    n = 0
    catalog = []
    for task_dir in sorted(p for p in SRC.iterdir() if p.is_dir()):
        meta_path = task_dir / "task.json"
        if not meta_path.exists():
            continue
        dest = out / task_dir.name
        dest.mkdir(parents=True)
        for name in PUBLIC_FILES:
            src_f = task_dir / name
            if not src_f.exists():
                raise SystemExit(f"missing required file {src_f}")
            shutil.copy2(src_f, dest / name)
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        catalog.append(
            {
                "id": meta["id"],
                "title": meta.get("title"),
                "tags": meta.get("tags", []),
                "provenance": meta.get("provenance"),
            }
        )
        n += 1

    # Lineage without private notes beyond catalog
    (out / "TASKS.json").write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    readme = f"""# code-reason public tasks

This package contains **{n}** code-reasoning tasks for evaluation.

Each task folder has:
- `task.json` — metadata
- `prompt.md` — model-facing specification
- `tests.py` — executable grader (imports `solution`)

**Reference solutions are intentionally omitted** (private / holdout / organizer-only).

## Metric (v0.1)

Pass rate: fraction of tasks whose tests exit 0 on the extracted model solution.

## Not included

- `reference.py` gold solutions
- Closed API credentials
- Private holdout split (if any)
"""
    (out / "README.md").write_text(readme, encoding="utf-8")
    print(f"Exported {n} tasks → {out}")
    return n


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--out",
        type=Path,
        default=REPO / "dist" / "kaggle_public" / "tasks",
        help="Output directory",
    )
    args = p.parse_args()
    export(args.out)


if __name__ == "__main__":
    main()
