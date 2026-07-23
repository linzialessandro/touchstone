# Touchstone — competition design

## Honest purpose

**Touchstone** is a Kaggle **AI coding-reasoning** benchmark: models write Python; **executable unit tests** grade them.

The goal is **not** “Grok 4.5 vs open models on the leaderboard.”

The goal is:

> **Grok wins as a *benchmark designer*** — Touchstone is a serious, useful, interesting coding-reasoning arena on Kaggle that open models compete on, and that success showcases design quality (with Grok in the design loop).

| Wins as… | Meaning |
|----------|---------|
| **Designer (Grok + you)** | The benchmark is credible, adopted, hard to game, worth running |
| **Competitor (open models only)** | Ranked by pass rate on executable tests |

## One-sentence pitch

Executable coding tasks for **open-weight models** on Kaggle; **designed with Grok**; Grok is **not** a leaderboard entry.

## Roles

| Role | Who | Does |
|------|-----|------|
| **Design** | You + Grok | Spec, metric, tasks, integrity, packaging, narrative |
| **Competitors** | **Open-weight models only** | Generate solutions; scored by tests |
| **Organizer** | You | Host dataset, holdout, Benchmark page, publish open-model results |
| **Participants** | Humans on Kaggle | Run open models on free GPU / Benchmarks UI |

**Grok does not compete on Touchstone.** No frontier model track on the official leaderboard.

## Track (single competitive track)

| Track | Models | Where |
|-------|--------|--------|
| **Open** | Qwen, Llama, Phi, Mistral, DeepSeek-Coder, … | **Kaggle free GPU** / Community Benchmarks |

Metric: **pass rate** = fraction of tasks with tests green.

## Integrity

1. Same prompts, system message, temperature, and tests for every **open** competitor.  
2. No hidden reshaping of the suite after seeing results.  
3. Publish run artifacts when claiming open-model ranks.  
4. Mock 100% is plumbing, never a model score.  
5. Holdout stays private until a real private LB exists.  
6. Do **not** list Grok (or other closed APIs) as official competitors.

## Metric

**Primary:** `pass_rate = n_pass / n_tasks`  
**Reported:** fails, errors/timeouts, optional per-tag rates  

## Suite shape

| Split | Role |
|-------|------|
| Public (~22) | Dataset + public scores |
| Holdout (~10) | Organizer strength / private score |

## “Designer win” success criteria

Touchstone (and Grok’s role in designing it) “wins” if:

1. The Benchmark + dataset are live and understandable.  
2. Multiple open models are scored fairly on free Kaggle GPU.  
3. Tasks are hard enough to separate weak vs strong open models.  
4. The metric is trusted (executable, documented contamination/holdout story).  
5. Others can run and cite the bench without special casing closed models.

## Narrative (use this publicly)

> **Touchstone** is an executable coding-reasoning benchmark for **open-weight models** on Kaggle.  
> It was **designed with Grok**. Grok **does not enter** the leaderboard.  
> The win for Grok is **design quality** of the arena, not a model score.

## Links

| Asset | URL |
|-------|-----|
| GitHub | https://github.com/linzialessandro/touchstone |
| Kaggle Benchmark | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| Dataset | `alessandrolinzi/touchstone` |

## Roadmap

| Gate | Status |
|------|--------|
| Honest designer-vs-competitor roles | done |
| Suite + open-only competitive track | done |
| GitHub live | done |
| Dataset upload + open GPU baselines | next |
| Stronger tasks if open models saturate | later |
