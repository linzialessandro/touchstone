# code-reason

**Provisional name** — harness-first **code-reasoning** evaluation suite for a research-engineering portfolio.

> Interview me relentlessly about every aspect of this until we reach a shared understanding…  
> This repo is the **execution** of that bet: a small, honest, runnable measurement system.

## What this is

- A **thin custom Python harness** you own: `Task` → `Attempt` → `Grade` → `Run`
- **Executable graders** (subprocess + tests), not LLM-as-judge
- A **hybrid task provenance** policy (original core + documented transforms)
- Explicit **contamination / limitations** docs — method is part of the product

## What this is not (yet)

- A large leaderboard or paper
- A web “arena” product
- A wrapper around HumanEval / LiveCodeBench as the product itself
- Proof of AGI, general reasoning, or model rankings from 3 toy tasks

## Quickstart

Requires Python 3.11+.

```bash
cd /path/to/Grill-me-test
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# List tasks
code-reason list-tasks

# Offline plumbing test (mock returns golden solutions)
code-reason run --provider mock

# Grade a local file (ownership drill)
code-reason grade-file 001_sliding_window_max \
  tasks/v0_1/001_sliding_window_max/reference.py
```

### Live baseline (Grok or Gemini)

```bash
cp .env.example .env
# Edit .env: set XAI_API_KEY or GEMINI_API_KEY

# Grok
export XAI_API_KEY=...
code-reason run --provider grok --model grok-3-mini

# Gemini
export GEMINI_API_KEY=...
code-reason run --provider gemini --model gemini-2.0-flash
```

Run JSON artifacts land in `runs/` (gitignored).

## Layout

```
src/code_reason/          # harness (own this)
  models.py               # Task, Attempt, Grade, Run
  loader.py               # discover tasks
  extract.py              # code fence extraction
  grader.py               # deterministic tests
  runner.py               # batch eval
  providers/              # mock | grok | gemini
  cli.py                  # code-reason entrypoint
tasks/v0_1/               # versioned task set + LINEAGE.md
docs/                     # contamination, ownership, bet summary
FREE_MONTH.md             # August sprint plan
runs/                     # local run artifacts
```

## Adding a task

1. Create `tasks/v0_1/<id>/` with `task.json`, `prompt.md`, `tests.py`, optional `reference.py`
2. Add a row to `tasks/v0_1/LINEAGE.md`
3. Answer contamination questions in `docs/contamination.md`
4. `code-reason grade-file <id> path/to/reference.py` must **pass**
5. A deliberately broken solution must **fail**

## Career context

See `docs/BET.md` and `FREE_MONTH.md`. Short version: build toward a **research eng** role in **reasoning/evals**, default job start after the school year, remote Udine preferred.

## License

MIT (harness). Dataset/task terms: still original small set; revisit if you ingest external seeds.
