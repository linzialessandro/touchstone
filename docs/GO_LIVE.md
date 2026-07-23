# Go-live — Touchstone

## Honest goal

Build a **Kaggle AI coding-reasoning benchmark** and enter **Grok 4.5** so it can **compete and possibly win** against open models under the **same** executable tests.

| Track | Where |
|-------|--------|
| Open field | Kaggle free GPU |
| Grok 4.5 | Frontier scoring (`XAI_API_KEY`) or Benchmark UI if supported |

## Live links

| Asset | URL |
|-------|-----|
| GitHub | https://github.com/linzialessandro/touchstone |
| Kaggle Benchmark | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| Dataset | `alessandrolinzi/touchstone` after upload |

## Checklist

- [x] Suite + harness + honest docs  
- [ ] Code on GitHub (`main` pushed)  
- [ ] Dataset uploaded  
- [ ] Open models scored on Kaggle GPU  
- [ ] Grok 4.5 scored on same public split  
- [ ] Benchmark page linked to dataset + results  

## Commands

```bash
# package
python scripts/package_kaggle.py
python scripts/package_kaggle.py --upload

# frontier Grok (when XAI_API_KEY in .env)
pip install -e ".[frontier]"
code-reason run -p grok -m grok-4.5
python scripts/build_leaderboard.py
```

Open models: **not** on this laptop — use Kaggle GPU notebook.
