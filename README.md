# Touchstone

**Executable AI coding-reasoning benchmark** — models write Python; **unit tests** grade.

| | |
|--|--|
| **GitHub** | https://github.com/linzialessandro/touchstone |
| **Kaggle Benchmark** | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| **Kaggle Dataset** | `alessandrolinzi/touchstone` |

## Why this exists (honest)

Favourite topic: **AI coding / reasoning benchmarks** on **Kaggle**.

**Goal:** put **Grok 4.5** on this leaderboard as a real competitor and **possibly win** — against a strong open-weight field — under a metric that is hard to game.

| Track | Who | Where |
|-------|-----|--------|
| **Open** | Qwen, Llama, Phi, Mistral, DeepSeek-Coder, … | **Kaggle free GPU** |
| **Frontier** | **Grok 4.5** | Same tasks/tests (API / organizer scoring) |

Same prompts. Same harness. Same tests. If Grok loses, we publish that too.

## Hardware

- **Open-model scoring:** Kaggle free GPU only (this laptop is not used for HF baselines).  
- **Local:** edit suite, `validate_suite` / mock plumbing, package + upload dataset.  
- **Grok 4.5:** frontier scoring when `XAI_API_KEY` is set (not free Kaggle notebooks).

## Quickstart (local — no model race)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

code-reason list-tasks
code-reason run --provider mock
python scripts/validate_suite.py
python scripts/package_kaggle.py
```

## Score models

**Open (Kaggle GPU):** attach dataset → run `baseline_notebook.ipynb` → swap models.  

**Grok 4.5 (frontier):**

```bash
pip install -e ".[frontier]"
# .env → XAI_API_KEY=...
code-reason run -p grok -m grok-4.5
python scripts/build_leaderboard.py
```

## Suite

| Item | Value |
|------|--------|
| Full local suite | **32** tasks |
| Public (Kaggle package) | **22** |
| Holdout | **10** |
| Metric | Pass rate (executable tests) |

## Docs

| Doc | Topic |
|-----|--------|
| [docs/COMPETITION.md](docs/COMPETITION.md) | Win condition, tracks, integrity |
| [docs/GO_LIVE.md](docs/GO_LIVE.md) | Push / upload / GPU steps |
| [docs/KAGGLE.md](docs/KAGGLE.md) | Dataset + Benchmarks |
| [docs/NAME.md](docs/NAME.md) | Why “Touchstone” |
| [docs/BET.md](docs/BET.md) | Career framing |

## License

MIT (harness). Task package default license in metadata: CC0.
