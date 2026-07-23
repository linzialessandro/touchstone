# Touchstone — competition design

## Honest purpose

**Touchstone** is a Kaggle-facing **AI coding / reasoning** benchmark: models write Python; **executable unit tests** grade them.

The personal goal behind the project is straightforward:

> **Get Grok 4.5 to compete on this benchmark (and related Kaggle surfaces) and possibly win** — on a topic I care about: coding-reasoning evals — under a metric that is hard to fake.

That only means something if the bar is fair: **same tasks, same harness, same pass/fail tests** for every model, including Grok 4.5. No private prompts for Grok, no dropping tasks after seeing scores.

## One-sentence pitch

Executable coding tasks for models on Kaggle; **open weights fill the field**; **Grok 4.5 is a competitor we want at the top**.

## Roles

| Role | Who | Does |
|------|-----|------|
| **Organizer / author** | You | Suite, holdout, packaging, honesty of the metric |
| **Design assistance** | Grok (and tools) | Help design tasks, rules, docs — *not* a free pass on the LB |
| **Field (open track)** | Open-weight models | Primary free path: Kaggle GPU / Community Benchmarks |
| **Competitor (frontier)** | **Grok 4.5** | Scored on the **same** public protocol; target champion |
| **Other frontier** | Optional later | Same rules if ever added |

Grok is **not** “above” the competition. It is a model we **enter** into the comparison because we want it to **win fairly**.

## Two tracks (same metric)

| Track | Models | Where runs happen | Leaderboard |
|-------|--------|-------------------|-------------|
| **Open** | Qwen, Llama, Phi, Mistral, DeepSeek-Coder, … | **Kaggle free GPU** / Benchmarks UI | Always published |
| **Frontier** | **Grok 4.5** (xAI API) | Organizer machine or any path Kaggle allows for that model | Published next to open results |

Metric for both: **pass rate** = fraction of tasks with tests green.

Open track does not require a paid API. Frontier Grok runs need `XAI_API_KEY` (or whatever Kaggle supports for that model later).

## Integrity (non-negotiable if “winning” is to mean anything)

1. Same `prompt.md`, system message, temperature policy, and `tests.py` for all models.  
2. No task-specific prompts or hints for Grok.  
3. No silent removal of tasks Grok fails.  
4. Publish run artifacts (notebooks / JSON) when claiming ranks.  
5. Mock 100% is plumbing, never a model score.  
6. Holdout stays private until a true private LB exists.  

If Grok 4.5 loses to an open model on Touchstone, **report that**. The project is still a success as an honest bench.

## Metric

**Primary:** `pass_rate = n_pass / n_tasks`  
**Reported:** fails, errors/timeouts, optional per-tag rates  
**Future:** pass@k, private holdout score  

## Suite shape

| Split | Role |
|-------|------|
| Public (`splits/public.txt`, ~22 tasks) | Dataset + public scores |
| Holdout (`splits/holdout.txt`, ~10 tasks) | Organizer / private strength |

Local full suite: 32 tasks under `tasks/v0_1` (includes gold `reference.py` for authors only — never ship gold publicly).

## Baselines

See `baselines/registry.yaml`:

- **open** — field to beat  
- **frontier** — `grok-4.5` as the intended champion entry  

## Where this lives

| Asset | URL |
|-------|-----|
| GitHub | https://github.com/linzialessandro/touchstone |
| Kaggle Benchmark | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| Kaggle Dataset | `alessandrolinzi/touchstone` (after upload) |

## Narrative (use this publicly)

> **Touchstone** is an executable coding-reasoning benchmark on Kaggle.  
> Open-weight models compete on free GPU.  
> **Grok 4.5** is evaluated under the same tests; the goal is for it to **win on merit**, not by special casing.

## Roadmap

| Gate | Status |
|------|--------|
| Honest win-condition stated | done |
| Suite + harness + splits | done |
| GitHub + Benchmark shell | done |
| Dataset upload + GPU open baselines | next |
| Grok 4.5 full public-split score published | next (frontier) |
| Stronger / more discriminating tasks if Grok saturates | later |
