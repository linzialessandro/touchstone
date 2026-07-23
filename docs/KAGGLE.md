# Touchstone on Kaggle (Kaggle-first)

## Policy

**All open-model evaluation runs on Kaggle free GPU.**  
Local hardware is not used for inference.

## Live

| Surface | URL |
|---------|-----|
| **Benchmark** | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| **GitHub** | https://github.com/linzialessandro/touchstone |
| **Dataset** | upload → `alessandrolinzi/touchstone` |

## Best venue

| Priority | Surface | Role |
|----------|---------|------|
| **1** | [Your Benchmark](https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone) | Native LLM/code eval leaderboards |
| **2** | Dataset `…/touchstone` | Ship public tasks + harness + notebook |
| **3** | Community Competition (optional later) | Human notebook races |

Docs: https://www.kaggle.com/docs/benchmarks  

## Local vs Kaggle

| Action | Where |
|--------|--------|
| Edit tasks, `validate_suite`, package zip | Local |
| `hf` / multi-model baselines / leaderboard numbers | **Kaggle GPU only** |
| Upload dataset | Local CLI → your Kaggle account |

## Upload dataset (you run this)

```bash
source .venv/bin/activate
python scripts/package_kaggle.py
python scripts/package_kaggle.py --upload
```

## GPU baseline workflow

1. New Notebook → **GPU on**  
2. Add data → **touchstone**  
3. Run `baseline_notebook.ipynb`  
4. Change `CODE_REASON_MODEL` for other open models  
5. Save version / share as baseline  

### Secrets on Kaggle (not local `.env`)

For gated HF models, add **Kaggle Notebook Secret** `HF_TOKEN` (Add-ons → Secrets).  
Do not rely on laptop `.env` inside Kaggle.

## Package layout (`dist/kaggle_public/`)

- `tasks/` public only (no gold, no holdout)  
- `code_reason/` harness  
- `baseline_notebook.ipynb`  
- `sample_submission.csv`  

Full go-live steps: [`GO_LIVE.md`](GO_LIVE.md).
