# Touchstone

**Executable AI coding-reasoning benchmark** on Kaggle.  
Models write Python; **unit tests** grade.

| | |
|--|--|
| **GitHub** | https://github.com/linzialessandro/touchstone |
| **Kaggle Benchmark** | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| **Dataset** | https://www.kaggle.com/datasets/alessandrolinzi/touchstone |
| **First task** | https://www.kaggle.com/benchmarks/tasks/alessandrolinzi/ts-partition |

## What this project is

| Layer | Role |
|-------|------|
| **Grok 4.5** | **Benchmark designer** — showcase designing code-reasoning evals that score *other* models |
| **Touchstone** | The **product** that **competes on Kaggle** (Community Benchmark + dataset) |
| **Models on the LB** | Free Kaggle catalog models (open **or** closed when free under Daily AI Quota) |

> Designed with Grok 4.5. The win is **design quality** and **project standing on Kaggle**, not a branded “Grok vs open weights” race — though any free catalog model may appear on the board.

## Hardware

- **Model scoring:** Kaggle Benchmarks Model Proxy / free GPU notebooks (not a weak laptop).  
- **Local:** edit suite, validate gold tests, package dataset, CLI push/run tasks.  

## Quickstart (local)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

code-reason list-tasks
code-reason run --provider mock
python scripts/validate_suite.py
python scripts/package_kaggle.py
```

## Kaggle Benchmarks CLI

```bash
kaggle benchmarks auth -y
kaggle benchmarks tasks push ts-partition -f benchmark_tasks/ts_partition.py -d alessandrolinzi/touchstone --wait
kaggle benchmarks tasks run ts-partition -m deepseek-v3.1 --wait
kaggle benchmarks tasks publish ts-partition
```

Attach tasks and models in the **benchmark UI**; fair use on Daily AI Quota.

## Suite

| Item | Value |
|------|--------|
| Full local suite | **32** tasks |
| Public package | **22** |
| Holdout | **10** |
| Live Kaggle task | `ts-partition` (stable_partition + executable checks) |

## Docs

| Doc | Topic |
|-----|--------|
| [docs/COMPETITION.md](docs/COMPETITION.md) | Designer vs project vs models |
| [docs/GO_LIVE.md](docs/GO_LIVE.md) | Ship checklist |
| [docs/KAGGLE.md](docs/KAGGLE.md) | Dataset + Benchmarks |
| [docs/NAME.md](docs/NAME.md) | Why “Touchstone” |
| [docs/BET.md](docs/BET.md) | Career framing |

## License

MIT (harness). Task package metadata default: CC0.
