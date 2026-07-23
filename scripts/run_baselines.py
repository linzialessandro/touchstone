#!/usr/bin/env python3
"""Run baselines from baselines/registry.yaml (open models only).

Grok wins as benchmark designer, not as a scored competitor.
Open models: prefer Kaggle free GPU (docs/GO_LIVE.md).

Examples:

    python scripts/run_baselines.py --track plumbing
    # open on Kaggle GPU preferred; local only with TOUCHSTONE_ALLOW_LOCAL_HF=1
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from code_reason.providers import get_provider  # noqa: E402
from code_reason.runner import run_eval, save_run  # noqa: E402


def load_registry(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--registry", type=Path, default=REPO / "baselines" / "registry.yaml")
    p.add_argument(
        "--track",
        choices=["open", "plumbing", "all"],
        default="plumbing",
        help="open = OSS competitors; plumbing = mock",
    )
    p.add_argument("--only", action="append", default=[], help="Model id filter (repeatable)")
    p.add_argument("--task", action="append", default=None, help="Task id filter (repeatable)")
    p.add_argument("--out", type=Path, default=REPO / "runs")
    args = p.parse_args()

    reg = load_registry(args.registry)
    jobs: list[tuple[str, str, str]] = []

    if args.track in ("plumbing", "all"):
        jobs.append(("plumbing", "mock", "mock-golden"))

    if args.track in ("open", "all"):
        if os.environ.get("TOUCHSTONE_ALLOW_LOCAL_HF", "").strip() not in ("1", "true", "yes"):
            print(
                "Refusing local open-model runs (use Kaggle free GPU).\n"
                "See docs/GO_LIVE.md. Override: TOUCHSTONE_ALLOW_LOCAL_HF=1",
                file=sys.stderr,
            )
            if args.track == "open":
                return 2
        else:
            for m in reg["tracks"]["open"]["models"]:
                jobs.append(("open", "hf", m["id"]))

    if args.only:
        allow = set(args.only)
        jobs = [j for j in jobs if j[2] in allow or (j[1] == "mock" and "mock" in allow)]

    if not jobs:
        print("No jobs matched.", file=sys.stderr)
        return 1

    print(f"Jobs: {len(jobs)}")
    for track, provider, model in jobs:
        print(f"\n=== [{track}] {provider} / {model} ===")
        os.environ["CODE_REASON_PROVIDER"] = provider
        prov = get_provider(provider)
        run = run_eval(prov, model, task_ids=args.task)
        path = save_run(run, args.out)
        s = run.summary
        rate = f"{s.pass_rate:.1%}" if s.pass_rate is not None else "n/a"
        print(f"pass_rate={rate} pass={s.n_pass} fail={s.n_fail} error={s.n_error} → {path}")

    print("\nDone. Build leaderboard with: python scripts/build_leaderboard.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
