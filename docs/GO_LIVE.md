# Go-live — Touchstone

## Honest goal

**Grok wins as benchmark designer** — Touchstone is a credible Kaggle coding-reasoning arena.  
**Open-weight models** are the only competitors on the leaderboard.

## Live links

| Asset | URL |
|-------|-----|
| GitHub | https://github.com/linzialessandro/touchstone |
| Kaggle Benchmark | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| Dataset | `alessandrolinzi/touchstone` (after upload) |

## Checklist

- [x] Suite + harness + designer-vs-competitor docs  
- [x] Code on GitHub  
- [ ] Dataset uploaded  
- [ ] Open models scored on Kaggle GPU  
- [ ] Benchmark page populated (tasks, description, links)  

## Commands

```bash
python scripts/package_kaggle.py
python scripts/package_kaggle.py --upload   # you run — publishes dataset
```

Open-model scoring: **Kaggle free GPU only** (not this laptop).
