# Touchstone — competition design

## Honest purpose

**Touchstone** is a Kaggle **AI coding-reasoning** benchmark: models write Python; **executable unit tests** grade them.

### What “wins”

| Winner | Meaning |
|--------|---------|
| **Grok 4.5 (designer)** | Showcase that Grok can **design** a serious code-reasoning bench that evaluates *other* models |
| **Touchstone (the project)** | Compete on Kaggle as a **Community Benchmark** — adoption, clarity, useful leaderboards |
| **Models on the LB** | Whatever free catalog models we run (open *or* closed) — ranked fairly by pass rate |

This is **not** “Grok 4.5 vs Qwen on the leaderboard as the product story.”  
It **is** “Grok designs the arena; many models get scored; the **project** competes for relevance on Kaggle.”

### Free catalog policy

If Kaggle Benchmarks lets us run a model **for free** (Daily AI Quota / Model Proxy), we **may** include it — open **or** proprietary (DeepSeek, Qwen, Gemini, Claude, Grok-as-subject, etc.).

- Prefer diverse, interesting comparisons.  
- Fair use: small batches, respect rate limits.  
- Optional: tag or section open vs proprietary later; not required day one.

## One-sentence pitch

Executable coding-reasoning tasks on Kaggle that score free catalog models — **designed with Grok 4.5** to show strong **benchmark design** for code reasoning.

## Roles

| Role | Who |
|------|-----|
| **Design** | You + **Grok 4.5** (product narrative: design skill on code-reasoning evals) |
| **Subjects** | Models on the LB (free Kaggle catalog) |
| **Organizer** | You (suite, holdout, packaging, UI, fair use) |
| **Venue** | Kaggle Community Benchmarks + dataset + GitHub |

## Metric

**Primary:** pass rate / pass-fail on executable tests (no LLM-as-judge for core score).  
**Integrity:** same prompts and tests for every model; publish methods; holdout stays private until used properly.

## Suite

| Split | Role |
|-------|------|
| Public | Dataset + public tasks (e.g. `ts-partition`) |
| Holdout | Organizer-only strength |

## Links

| Asset | URL |
|-------|-----|
| GitHub | https://github.com/linzialessandro/touchstone |
| Kaggle Benchmark | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| Dataset | https://www.kaggle.com/datasets/alessandrolinzi/touchstone |
| First task | https://www.kaggle.com/benchmarks/tasks/alessandrolinzi/ts-partition |

## Narrative (public)

> **Touchstone** is a coding-reasoning benchmark on Kaggle.  
> Models solve Python tasks; unit tests decide.  
> **Designed with Grok 4.5** — the showcase is **designing the evaluation**, not Grok topping the scoreboard as a competitor brand story.  
> We score free catalog models (open and closed) under one fair protocol.  
> The **project** competes on Kaggle as a Community Benchmark worth running and citing.

## Roadmap

| Gate | Status |
|------|--------|
| Honest designer / project framing | done |
| Dataset + first executable task | done |
| Multi-model free catalog runs | in progress |
| More Touchstone tasks | next |
| Public benchmark polish | next |
