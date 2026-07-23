# Self-study map

**North star:** research engineer in **reasoning & evals**, portfolio = this **open-weight** benchmark + Kaggle package.  
**Roles:** Grok helped **design** the competition; **only open models compete**.

## Three tracks

| Track | Purpose | Artifacts |
|-------|---------|-----------|
| **A. Eval craft** | Competition-grade measurement | Tasks, holdouts, contamination, baselines on OSS models |
| **B. Software ownership** | RE interviews | `src/code_reason/*` you can teach |
| **C. Fundamentals** | Screens | Python, algorithms, systems (phased) |

## Model evaluation practice (primary lab = Kaggle GPU)

**Do not score models on the laptop.** Use Kaggle free GPU:

1. Dataset **touchstone** attached  
2. `baseline_notebook.ipynb` (or forks per model)  
3. Log pass rate, failures, OOM → rewrite tasks locally  

Local: only `validate_suite` / mock plumbing / packaging.

## Weekly rhythm (~10–12 h school year)

1. **Calibrate / author** — harden tasks; run one OSS model subset  
2. **Own** — one harness module without the agent  
3. **Later phases** — interview drills; applications toward W2  

## Kaggle readiness (personal checklist)

See `docs/KAGGLE.md`. Short version: public export without refs → baseline notebook → holdout → only then competition framing.

## Health

Deep blocks beat hero weeks. The suite improves by **iteration on failures**, not by counting tasks alone.
