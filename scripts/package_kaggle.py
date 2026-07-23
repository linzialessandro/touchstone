#!/usr/bin/env python3
"""Build a complete Kaggle dataset package for Touchstone.

Contents:
  - public tasks (no reference.py)
  - harness source (src/code_reason)
  - sample_submission.csv
  - baseline notebook
  - dataset-metadata.json
  - README for participants

Usage:
  python scripts/package_kaggle.py
  python scripts/package_kaggle.py --upload
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]
TASKS_SRC = REPO / "tasks" / "v0_1"
PUBLIC_SPLIT = REPO / "splits" / "public.txt"
HOLDOUT_SPLIT = REPO / "splits" / "holdout.txt"
OUT = REPO / "dist" / "kaggle_public"
PUBLIC_FILES = ("task.json", "prompt.md", "tests.py")


def read_split(path: Path) -> list[str]:
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        ids.append(s)
    return ids


def export_tasks(task_ids: list[str], dest_root: Path) -> list[dict]:
    dest_root.mkdir(parents=True, exist_ok=True)
    catalog: list[dict] = []
    for tid in task_ids:
        src = TASKS_SRC / tid
        if not src.is_dir():
            raise SystemExit(f"missing task dir: {src}")
        dest = dest_root / tid
        dest.mkdir(parents=True, exist_ok=True)
        for name in PUBLIC_FILES:
            f = src / name
            if not f.exists():
                raise SystemExit(f"missing {f}")
            shutil.copy2(f, dest / name)
        meta = json.loads((src / "task.json").read_text(encoding="utf-8"))
        catalog.append(
            {
                "id": meta["id"],
                "title": meta.get("title"),
                "tags": meta.get("tags", []),
                "difficulty": meta.get("difficulty", "medium"),
            }
        )
    return catalog


def write_sample_submission(task_ids: list[str], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["task_id", "passed"])
        for tid in task_ids:
            w.writerow([tid, 0])


def copy_harness(dest: Path) -> None:
    src = REPO / "src" / "code_reason"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        src,
        dest,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
    )


def write_readme(path: Path, n_public: int, n_holdout: int, username: str) -> None:
    path.write_text(
        f"""# Touchstone (public package)

**Touchstone** — executable coding benchmark for **open-weight** models.

A touchstone is a classical test of genuineness: models write Python; **unit tests** grade.

- **Topic:** AI coding / reasoning
- **Competitors:** open-weight models only (Kaggle free GPU)
- **Design:** built with Grok — Grok does **not** compete on the leaderboard
- **Metric:** pass rate = fraction of tasks whose executable tests pass

## Package contents

| Path | Description |
|------|-------------|
| `tasks/` | **{n_public}** public tasks (`prompt.md`, `tests.py`, `task.json`) — **no gold solutions** |
| `code_reason/` | Eval harness (Task → Attempt → Grade → Run) |
| `sample_submission.csv` | `task_id,passed` template |
| `baseline_notebook.ipynb` | Starter notebook for Kaggle GPU |
| `TASKS.json` | Task catalog |

Private holdout: **{n_holdout}** tasks are **not** in this package (organizer-only scoring).

## Participant workflow (Kaggle)

1. Enable **GPU** on the notebook.
2. Add this dataset as input.
3. Install deps, load an open model (e.g. Qwen2.5-1.5B-Instruct).
4. For each task: generate Python solution → run `tests.py` → record pass/fail.
5. Write `submission.csv` with columns `task_id,passed` (0/1).

## Harness import on Kaggle

```python
import sys
sys.path.insert(0, "/kaggle/input/touchstone")  # folder name may match dataset slug
from code_reason.providers import get_provider
from code_reason.runner import run_eval
```

## Integrity

- Do not use closed APIs for official competitive submissions.
- Do not train on holdout (holdout is not public).
- Gold `reference.py` files are never shipped here.

Dataset slug: `{username}/touchstone`  
Also see Kaggle **Community Benchmarks** for native model leaderboards.
""",
        encoding="utf-8",
    )


def write_notebook(path: Path, dataset_slug: str) -> None:
    nb = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Touchstone — baseline notebook\n",
                    "\n",
                    "Open-weight models only. **Designed with Grok** — Grok does not compete on the leaderboard.\n",
                    "\n",
                    "1. Enable GPU\n",
                    f"2. Attach dataset `{dataset_slug}`\n",
                    "3. Run all cells\n",
                ],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "outputs": [],
                "execution_count": None,
                "source": [
                    "from pathlib import Path\n",
                    "import sys, os\n",
                    "\n",
                    f"DATA = Path('/kaggle/input/{dataset_slug.split('/')[-1]}')\n",
                    "if not DATA.exists():\n",
                    "    DATA = Path('.')\n",
                    "TASKS = DATA / 'tasks'\n",
                    "sys.path.insert(0, str(DATA))\n",
                    "print('DATA', DATA, 'tasks', TASKS.exists())\n",
                ],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "outputs": [],
                "execution_count": None,
                "source": [
                    "%pip install -q transformers accelerate sentencepiece pydantic\n",
                ],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "outputs": [],
                "execution_count": None,
                "source": [
                    "import os\n",
                    "os.environ.setdefault('CODE_REASON_PROVIDER', 'hf')\n",
                    "os.environ.setdefault('CODE_REASON_MODEL', 'Qwen/Qwen2.5-1.5B-Instruct')\n",
                    "os.environ.setdefault('CODE_REASON_MAX_NEW_TOKENS', '1024')\n",
                    "os.environ.setdefault('CODE_REASON_TEMPERATURE', '0.0')\n",
                    "\n",
                    "from code_reason.providers import get_provider\n",
                    "from code_reason.runner import run_eval\n",
                    "\n",
                    "MODEL = os.environ['CODE_REASON_MODEL']\n",
                    "provider = get_provider('hf')\n",
                    "\n",
                    "# Full public suite (may take a while on free GPU)\n",
                    "run = run_eval(provider, MODEL, tasks_dir=TASKS)\n",
                    "print(run.summary)\n",
                ],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "outputs": [],
                "execution_count": None,
                "source": [
                    "import csv\n",
                    "from pathlib import Path\n",
                    "out = Path('/kaggle/working/submission.csv')\n",
                    "if not out.parent.exists():\n",
                    "    out = Path('submission.csv')\n",
                    "with out.open('w', newline='') as f:\n",
                    "    w = csv.writer(f)\n",
                    "    w.writerow(['task_id', 'passed'])\n",
                    "    for g in run.grades:\n",
                    "        w.writerow([g.task_id, 1 if g.status.value == 'pass' else 0])\n",
                    "print('wrote', out)\n",
                    "print('pass_rate', run.summary.pass_rate)\n",
                ],
            },
        ],
    }
    path.write_text(json.dumps(nb, indent=2), encoding="utf-8")


def build(username: str) -> Path:
    public_ids = read_split(PUBLIC_SPLIT)
    holdout_ids = read_split(HOLDOUT_SPLIT)
    # consistency: no overlap
    overlap = set(public_ids) & set(holdout_ids)
    if overlap:
        raise SystemExit(f"split overlap: {sorted(overlap)}")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    catalog = export_tasks(public_ids, OUT / "tasks")
    (OUT / "TASKS.json").write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    (OUT / "splits").mkdir()
    shutil.copy2(PUBLIC_SPLIT, OUT / "splits" / "public.txt")
    # do not copy holdout task content; only count for README honesty
    (OUT / "splits" / "README.md").write_text(
        f"Public tasks: {len(public_ids)}. Holdout tasks (not packaged): {len(holdout_ids)}.\n",
        encoding="utf-8",
    )

    copy_harness(OUT / "code_reason")
    write_sample_submission(public_ids, OUT / "sample_submission.csv")
    slug = f"{username}/touchstone"
    write_readme(OUT / "README.md", len(public_ids), len(holdout_ids), username)
    write_notebook(OUT / "baseline_notebook.ipynb", slug)

    meta = {
        "title": "Touchstone — public coding benchmark for open-weight models",
        "id": slug,
        "licenses": [{"name": "CC0-1.0"}],
    }
    (OUT / "dataset-metadata.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    # py.typed / init already in package
    print(f"Built {OUT}")
    print(f"  public tasks: {len(public_ids)}")
    print(f"  holdout (excluded): {len(holdout_ids)}")
    print(f"  slug: {slug}")
    return OUT


def upload(out: Path) -> None:
    # create or version
    r = subprocess.run(
        ["kaggle", "datasets", "create", "-p", str(out), "--dir-mode", "zip"],
        capture_output=True,
        text=True,
    )
    print(r.stdout)
    print(r.stderr)
    if r.returncode != 0 and "already exists" in (r.stdout + r.stderr).lower():
        r2 = subprocess.run(
            [
                "kaggle",
                "datasets",
                "version",
                "-p",
                str(out),
                "-m",
                "CodeReason Open public v0.2",
                "--dir-mode",
                "zip",
            ],
            capture_output=True,
            text=True,
        )
        print(r2.stdout)
        print(r2.stderr)
        if r2.returncode != 0:
            raise SystemExit(r2.returncode)
    elif r.returncode != 0:
        raise SystemExit(r.returncode)


def main() -> None:
    load_dotenv(REPO / ".env", override=True)
    if os.environ.get("KAGGLE_API_TOKEN") and not os.environ.get("KAGGLE_KEY"):
        os.environ["KAGGLE_KEY"] = os.environ["KAGGLE_API_TOKEN"]
    if os.environ.get("HF_TOKEN") and not os.environ.get("HUGGING_FACE_HUB_TOKEN"):
        os.environ["HUGGING_FACE_HUB_TOKEN"] = os.environ["HF_TOKEN"]

    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--upload", action="store_true", help="Upload/version dataset on Kaggle")
    p.add_argument(
        "--username",
        default=os.environ.get("KAGGLE_USERNAME", "").strip(),
        help="Kaggle username for dataset id",
    )
    args = p.parse_args()
    if not args.username:
        raise SystemExit("KAGGLE_USERNAME missing")
    out = build(args.username)
    if args.upload:
        upload(out)


if __name__ == "__main__":
    main()
