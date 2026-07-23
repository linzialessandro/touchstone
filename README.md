# Touchstone

**Executable AI coding-reasoning benchmark** for **open-weight models**.  
Models write Python; **unit tests** grade.

| | |
|--|--|
| **GitHub** | https://github.com/linzialessandro/touchstone |
| **Kaggle Benchmark** | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| **Kaggle Dataset** | `alessandrolinzi/touchstone` |

## Honest roles

| Role | Who |
|------|-----|
| **Benchmark design** | You + **Grok** — the “win” is a **good arena**, not a model score |
| **Competitors** | **Open-weight models only** (Qwen, Llama, Phi, Mistral, DeepSeek-Coder, …) |
| **Scoring venue** | **Kaggle free GPU** / Community Benchmarks |

> **Grok wins as designer.** Grok does **not** compete on the leaderboard.

## Hardware

- **Model scoring:** Kaggle free GPU only.  
- **Local:** edit suite, validate gold tests, package/upload dataset.  

## Quickstart (local — no LLM race)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

code-reason list-tasks
code-reason run --provider mock
python scripts/validate_suite.py
python scripts/package_kaggle.py
```

## Score open models (Kaggle GPU)

1. `python scripts/package_kaggle.py --upload` (your account)  
2. Notebook → GPU → attach **touchstone** → run `baseline_notebook.ipynb`  
3. Repeat for models in `baselines/registry.yaml`  

## Suite

| Item | Value |
|------|--------|
| Full local suite | **32** tasks |
| Public package | **22** |
| Holdout | **10** |
| Metric | Pass rate (executable tests) |
| Competitive track | Open-weight only |

## Docs

| Doc | Topic |
|-----|--------|
| [docs/COMPETITION.md](docs/COMPETITION.md) | Designer win vs open competitors |
| [docs/GO_LIVE.md](docs/GO_LIVE.md) | Upload / GPU steps |
| [docs/KAGGLE.md](docs/KAGGLE.md) | Dataset + Benchmarks |
| [docs/NAME.md](docs/NAME.md) | Why “Touchstone” |
| [docs/BET.md](docs/BET.md) | Career framing |

## License

MIT (harness). Task package metadata default: CC0.
