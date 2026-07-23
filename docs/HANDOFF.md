# Touchstone — full handoff (for a new conversation)

**Last updated:** 2026-07-23  
**Assume:** latest hard-task push/run pipeline completed successfully (4 hard + strengthened tasks published; models run; code on GitHub).

Use this file as the primary onboarding doc. Also read `docs/COMPETITION.md` for product philosophy.

---

## 1. What Touchstone is

| | |
|--|--|
| **Name** | **Touchstone** |
| **Product** | Executable **AI coding-reasoning** benchmark on **Kaggle Community Benchmarks** |
| **Metric** | Model writes Python → **unit tests / asserts run** → pass/fail (not LLM-as-judge for core score) |
| **Local package name** | Python package still `code_reason` (`code-reason` CLI); product brand is Touchstone |

### Product philosophy (source of truth)

| Layer | Role |
|-------|------|
| **Grok 4.5** | **Benchmark designer** — showcase designing evals that score *other* models on code reasoning |
| **Touchstone (project)** | Competes on **Kaggle** as a Community Benchmark + public dataset |
| **Models on the leaderboard** | Free Kaggle catalog models (open **or** closed when free under Daily AI Quota) |

**Not** the main story: Grok racing open weights as a branded “win the LB” competitor.  
**Is** the story: Grok-designed suite; fair executable metric; project has standing on Kaggle.

Public one-liner:

> Designed with Grok 4.5 to showcase strong **benchmark design** for code reasoning. Free catalog models are scored under one protocol. The **project** competes on Kaggle.

---

## 2. Live links

| Asset | URL |
|-------|-----|
| **GitHub** | https://github.com/linzialessandro/touchstone |
| **Kaggle Benchmark** | https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone |
| **Kaggle Dataset** | https://www.kaggle.com/datasets/alessandrolinzi/touchstone |
| **Local workspace** | `/Users/alessandro/antigravity/Grill-me-test` |

### Kaggle Benchmark tasks (public)

| Slug | Role | Difficulty |
|------|------|------------|
| `ts-partition` | Calibration (easy) | Easy — everyone often PASSes |
| `ts-wildcard` | Hard suite | Hard — stricter asserts |
| `ts-eval-expr` | Hard suite | Hard — stricter asserts |
| `ts-min-cover` | Hard suite | Hard — stricter asserts |
| `ts-accounts-merge` | Hard suite | Hard — stricter asserts |
| `ts-tree-codec` | Hard suite (newer) | Hard — hidden tree shapes |
| `ts-token-bucket` | Hard suite (newer) | Hard — hidden timing cases |
| `ts-kth-sorted` | Hard suite (newer) | Hard — empty/dup/range cases |

Task URLs follow:

`https://www.kaggle.com/benchmarks/tasks/alessandrolinzi/<slug>`

Ignore / do not use on the Touchstone board:

- `what-is-kaggle` — CLI smoke example only  
- `touchstone-stable-partition` — failed early versions; superseded by `ts-partition`

---

## 3. Why one easy task was not enough

With only `ts-partition`, almost every model scored **1.00** → no ranking.

**Comparison requires a suite:** overall ≈ (# tasks passed) / N.

After hard tasks were added, the board started to separate (e.g. one Qwen ~20% while others stayed high). **Further hard tasks + stricter asserts** are intentional to avoid a flat 100% ceiling among strong models.

---

## 4. Repository layout

```
Grill-me-test/   # local path; remote = linzialessandro/touchstone
├── README.md
├── pyproject.toml              # package code_reason / CLI code-reason
├── docs/
│   ├── HANDOFF.md              # THIS FILE
│   ├── COMPETITION.md          # philosophy & roles
│   ├── BET.md                  # career framing
│   ├── GO_LIVE.md              # short checklist
│   ├── KAGGLE.md               # dataset / benchmarks notes
│   ├── NAME.md                 # why “Touchstone”
│   ├── TASK_AUTHORING.md       # local suite authoring
│   ├── OWNERSHIP.md
│   ├── STUDY.md
│   └── contamination.md
├── benchmark_tasks/            # Kaggle Benchmarks @task Python files (CLI push)
│   ├── ts_partition.py         # easy calibration
│   ├── ts_wildcard.py
│   ├── ts_eval_expr.py
│   ├── ts_min_cover.py
│   ├── ts_accounts_merge.py
│   ├── ts_tree_codec.py
│   ├── ts_token_bucket.py
│   ├── ts_kth_sorted.py
│   └── touchstone_stable_partition.py  # legacy/broken attempts; prefer ts_partition
├── tasks/v0_1/                 # Full local suite (32 items) + reference.py gold
│   ├── LINEAGE.md
│   ├── 001_… through 032_…
│   └── (references are PRIVATE — never ship in public dataset)
├── splits/
│   ├── public.txt              # ~22 ids for public package
│   └── holdout.txt             # ~10 ids excluded from public zip
├── scripts/
│   ├── package_kaggle.py       # build/upload dataset zip
│   ├── validate_suite.py       # gold refs pass local tests
│   ├── run_baselines.py        # mock OK; local HF blocked unless override
│   ├── build_leaderboard.py
│   └── export_public_tasks.py
├── src/code_reason/            # harness: Task→Attempt→Grade→Run; providers mock|hf
├── baselines/registry.yaml
├── kaggle/dataset-metadata.json
├── dist/kaggle_public/         # build output (gitignored); regenerate with package script
├── example_task.py             # from kaggle b init (smoke)
├── kaggle_benchmarks_reference.md
└── .env                        # SECRETS — gitignored — never commit
```

---

## 5. Credentials

| Secret | Needed? | Purpose |
|--------|---------|---------|
| **Kaggle OAuth** (`kaggle auth login`) or API token | **Yes** | Dataset, Benchmarks CLI |
| **Model Proxy** (`kaggle b auth` / `init`) | **Yes** for `tasks run` | Short-lived; re-auth when expired (~hours) |
| **HF_TOKEN** | **No** for Benchmarks catalog runs | Only for HF/`transformers` notebooks or gated downloads |
| **XAI_API_KEY** | **No** for current path | Not used (Grok is designer, not required competitor) |

`.env` is gitignored. After `kaggle b init` / `auth`, Model Proxy vars are appended (`MODEL_PROXY_*`, `LLM_DEFAULT`, …).

Phone/Persona verification was required for Benchmarks API (403 until fixed). Dataset API worked earlier with `kaggle.json`.

---

## 6. Two parallel “task systems”

| System | What | Where |
|--------|------|--------|
| **Local suite** | 32 problems under `tasks/v0_1/` with `prompt.md`, `tests.py`, `reference.py` | Authoring + `validate_suite` |
| **Kaggle Benchmark tasks** | `@kbench.task` files in `benchmark_tasks/*.py` | Leaderboard / Model Proxy |

Kaggle does **not** auto-import `tasks/v0_1`. Each public LB task is a thin `kaggle_benchmarks` script that prompts the model and grades with `script_runner` + asserts (pattern of `ts_partition.py`).

### Working task pattern (creation must not crash)

- Soft-fail: `try/except` around `llm.prompt`; return `bool`  
- `extract_code` + `script_runner.run_code` with inline asserts  
- **No** hard `assert_true` that kills the notebook on model failure (that made early pushes ERRORED)  
- `.run(kbench.llm)` required at bottom  
- Push with `-d alessandrolinzi/touchstone` when dataset assets help (optional if prompt is embedded)

---

## 7. CLI cheat sheet

```bash
cd ~/antigravity/Grill-me-test   # or clone of linzialessandro/touchstone
source .venv/bin/activate

# Auth (repeat when Model Proxy expires)
kaggle auth login                 # if needed
kaggle benchmarks auth -y         # or: kaggle b init -y

# Push a task
kaggle benchmarks tasks push <slug> \
  -f benchmark_tasks/<file>.py \
  -d alessandrolinzi/touchstone \
  --wait -v

# Run models (fair use: small batches)
kaggle benchmarks tasks models
kaggle benchmarks tasks run <slug> -m deepseek-v3.1 -m gpt-oss-120b --wait -v

# Status / publish / download
kaggle benchmarks tasks status <slug>
kaggle benchmarks tasks publish <slug>
kaggle benchmarks tasks download <slug> -o ./bench_results

# Dataset package
python scripts/package_kaggle.py
python scripts/package_kaggle.py --upload   # title must be 6–50 chars

# Local harness (no LLM race on weak laptop)
python scripts/validate_suite.py
code-reason run -p mock
# Local HF full suite discouraged: TOUCHSTONE_ALLOW_LOCAL_HF=1 required for run_baselines --track open
```

**CLI cannot** attach tasks to the **benchmark collection** or make the **benchmark** public. That is **UI only** (Kaggle docs: tasks CLI ≠ managing benchmark collections).

---

## 8. UI workflow (critical)

### Add tasks to collection

1. https://www.kaggle.com/benchmarks/alessandrolinzi/touchstone  
2. **Add Tasks** → **Your tasks**  
3. Check: `ts-partition` + hard tasks (`ts-wildcard`, `ts-eval-expr`, `ts-min-cover`, `ts-accounts-merge`, `ts-tree-codec`, `ts-token-bucket`, `ts-kth-sorted`, …)  
4. **Do not** add `what-is-kaggle` or failed private tasks  

### Models on the leaderboard

- First attach of a task may open **Import model results** (“models already ran these tasks”) — best path.  
- Later: **+ Add Models** shows the **full catalog** → manually check models; may reuse completed runs (quota stays flat) or require **▶** to generate (uses **Daily AI Quota**, e.g. $10/day).  
- **Add Tasks** cannot re-import model runs for a task already on the board.

### Ranking

With multiple tasks, overall score ≈ **% of tasks passed** (e.g. 100 vs 20 when only easy task passes).  
If almost everyone is 100%, suite is **too easy** → add harder tasks / stricter hidden asserts (already the direction).

---

## 9. Models

### Catalog

```bash
kaggle benchmarks tasks models
```

~37 models as of 2026-07-23: Claude, Gemini, GPT-5.x, Qwen3, DeepSeek, Gemma, gpt-oss, GLM-5, Grok 4.20 variants, etc.

**Not in catalog:** Moonshot/Kimi, classic Mistral (use HF notebooks if needed).

### Fair-use model set used for hard tasks

Typically:

- `deepseek-v3.1`  
- `deepseek-r1-0528`  
- `gpt-oss-120b`  
- `gemma-4-31b-it` (and sometimes 26B)  
- `glm-5`  
- `qwen3-next-80b-a3b-thinking`  
- also: `qwen3-235b-a22b-instruct-2507` on earlier batches  

**Rate limits:** 429 heavy load / 503 unreachable — retry later, don’t spam.

### Free?

Benchmarks Model Proxy + Daily AI Quota ≈ free with limits. HF token not needed for catalog runs.

---

## 10. Dataset packaging

```bash
python scripts/package_kaggle.py
# builds dist/kaggle_public/
# title must be 6–50 chars: "Touchstone open coding benchmark"
# slug: alessandrolinzi/touchstone
# public tasks only (no reference.py, holdout excluded)
python scripts/package_kaggle.py --upload
```

Contents: `tasks/`, `code_reason/`, `baseline_notebook.ipynb`, `sample_submission.csv`, `TASKS.json`, `README.md`.

---

## 11. Local suite (32 tasks)

- `tasks/v0_1/` — full authoring suite with gold `reference.py`  
- `splits/public.txt` / `holdout.txt`  
- `python scripts/validate_suite.py` — all references must pass  

Kaggle Benchmark tasks are a **thin public subset** of that design, not a 1:1 upload of all 32.

---

## 12. Known issues & lessons

| Issue | Lesson |
|-------|--------|
| Early `touchstone-stable-partition` ERRORED on create | Hard asserts / crashes when default model fails → use soft `-> bool` |
| Flat 100% LB on one easy task | Need multi-task suite + hard items |
| Add Tasks won’t re-add `ts-partition` | Task already attached; use Add Models for more columns |
| Import wizard often only on first task attach | Later runs: Add Models or re-import if UI offers it |
| 403 on `benchmarks init` | Phone/identity verification; OAuth + verification fixed it |
| `zsh: command not found: #` | Don’t paste comment lines into shell |
| Dataset title > 50 chars | Kaggle rejects; use short title |
| HF token | Optional; not used for Model Proxy scoring |
| Agent environment | Sometimes blocks `tasks run` / upload; user runs those commands |

---

## 13. What to do in a new conversation

Paste something like:

> Continue **Touchstone** at `/Users/alessandro/antigravity/Grill-me-test` (GitHub `linzialessandro/touchstone`).  
> Read `docs/HANDOFF.md` and `docs/COMPETITION.md`.  
> Goal: Grok 4.5 as **benchmark designer**; project competes on Kaggle; free catalog models scored fairly.  
> Live: Benchmark + dataset + multi-task suite (`ts-partition` + hard tasks).  
> Next: [e.g. add more hard tasks / analyze pass-fail matrix / polish public description / stricter tests].

### Suggested next engineering work

1. Confirm all hard tasks appear on the **benchmark UI** and scores discriminate (not all 100%).  
2. If still too easy: more hidden tests or harder algorithms.  
3. Document per-task PASS/FAIL matrix from task compare pages.  
4. Optional: sections on LB (easy vs hard).  
5. Optional: GPU notebook baselines for HF models not in catalog (Mistral, etc.).  
6. Keep fair use on Daily AI Quota.

---

## 14. Agent / human safety

- Never commit `.env`  
- Never paste API tokens into chat  
- Prefer Kaggle for model scoring (not local GPU)  
- Designer narrative for Grok; do not reverse to “Grok must beat open models on our LB” unless the user explicitly changes philosophy again  

---

## 15. Quick status snapshot (end of handoff session)

| Item | State |
|------|--------|
| GitHub | Live, main pushed |
| Dataset | Live (`alessandrolinzi/touchstone`) |
| Benchmark shell | Live with description + GitHub/dataset links |
| Easy task | `ts-partition` on LB |
| Hard tasks | wildcard, eval-expr, min-cover, accounts-merge (+ tree/token/kth when pushes finished) |
| Multi-model runs | Open-leaning set + some closed free models |
| Discrimination | Started (e.g. some Qwen low overall); suite still may need more hardness |
| Local HF | Not required |
| HF_TOKEN | Not required for current path |

---

*End of handoff. Prefer this file over chat history.*
