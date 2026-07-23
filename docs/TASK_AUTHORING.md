# Task authoring guide

This project is a **measurement system**, not a leetcode clone dump. Every task should train either:

1. **Eval craft** — clear specs, adversarial tests, lineage, anti-cheat, or  
2. **Your engineering ownership** — code you can teach without an agent.

## Layout

```
tasks/v0_1/<id>/
  task.json      # id, title, tags, provenance, timeout
  prompt.md      # what the model sees
  tests.py       # executable grader (imports solution)
  reference.py   # private gold — for you + mock; strip for public releases
```

## Checklist

- [ ] Spec is unambiguous; edge cases listed  
- [ ] Tests cover happy path + edges + at least one anti-hardcode case  
- [ ] `reference.py` passes; empty file fails  
- [ ] Row added to `tasks/v0_1/LINEAGE.md`  
- [ ] You can explain why a wrong solution fails  
- [ ] `python scripts/validate_suite.py`  

## Commands

```bash
code-reason grade-file <id> tasks/v0_1/<id>/reference.py
python scripts/validate_suite.py
code-reason run --provider mock
```

## Design taste (for research-eng goals)

| Prefer | Avoid |
|--------|--------|
| Spec traps and multi-step constraints | Pure trivia one-liners |
| Deterministic graders | LLM-as-judge as default |
| Documented provenance | Silent copy of a famous statement |
| Small N of high-quality items | Inflated N of near-duplicates |

When you later publish (GitHub/Kaggle), ship **prompts + tests**, keep **references** private or in a closed split.
