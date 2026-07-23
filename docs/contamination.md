# Contamination, gaming, and limitations

This document is part of the **method** of the project, not an afterthought.

## What we claim (v0.1)

- We can run a **mid-size** code-reasoning suite (**25** tasks in `v0_1`) with **executable graders**.
- We record prompts, raw model outputs, extracted code, and grade details.
- We maintain **lineage notes** for tasks (`tasks/v0_1/LINEAGE.md`).
- Several tasks are **original APIs / rule variants**; some share *family* resemblance with public problems (useful for harness practice; not a claim of novelty for every item).

## What we do **not** claim (v0.1)

- That scores estimate “general reasoning” in the wild.
- That tasks are contamination-free against all pretraining data.
- That pass@1 on this suite is a public leaderboard.
- That LLM-as-judge is involved (it is not; graders are deterministic subprocess tests).
- That every task is research-novel (see lineage; plan holdouts before Kaggle/public launch).
- That scores from **closed APIs** are part of this product (open-weight / Kaggle path only).

## Threat model

| Threat | Example | Mitigations (now / next) |
|--------|---------|---------------------------|
| **Memorization** | Model recalls a famous leetcode solution | Prefer original wording; avoid identical public APIs when possible; expand with transforms; track seeds |
| **Hardcoded cheats** | `return [3,3,5,5,6,7]` for one example | Hidden cases in tests; multiple assertions; grow private holdouts |
| **Grader gaming** | Empty file that still “passes” | Fail closed on missing symbols; real assertions |
| **Train–test leakage** | Tasks posted publicly then trained on | Version splits; future canaries; document publish dates |
| **Flaky concurrency** | Race tests pass by luck | High iteration counts; may still be imperfect — document flakiness risk |
| **Prompt injection into harness** | Model writes files outside sandbox | v0.1 uses temp dir + subprocess; tighten isolation later |

## Canaries (planned)

- Hold out 5–10 tasks never in public README examples.
- Rotate a small private set each quarter.
- Record harness version + task set hash on every run artifact.

## How to add a task without lying

1. Write `prompt.md` + `tests.py` + `task.json` + lineage row.
2. Answer the three questions in `LINEAGE.md`.
3. Grade the **reference** solution with `code-reason grade-file`.
4. Grade at least one **broken** solution (must fail).
5. Only then run models.

## Limitations of the current harness

- No container sandbox (process isolation only).
- No multi-file project tasks yet.
- No statistical significance reporting.
- Mock provider embeds golden solutions for plumbing tests — **never** use mock scores as model quality.
