# Task lineage (v0.1)

Provenance policy (locked): **hybrid E**

| Priority | Kind | Rule |
|----------|------|------|
| 1 | `original` | Hand-authored or deep rewrite you fully understand |
| 2 | `transform` | Seed public idea systematically rewritten; document seed + transform steps |
| 3 | `synthetic_filtered` | LLM draft allowed; human accept/reject + owned tests |
| never | famous-bench wrap | May *compare* later; not the product |

## Current tasks

| id | provenance | notes |
|----|------------|-------|
| `001_sliding_window_max` | original | Classic algorithm; wording and tests authored for this harness (not a copy of a named contest PDF) |
| `002_parse_ini_sections` | original | Small parsing/spec-following task; original tests |
| `003_race_condition_fix` | original | Concurrency reasoning; fix a broken pattern; original tests |

## Contamination threat model (v0.1 sketch)

See `docs/contamination.md`. For each new task, answer before merge:

1. Could a model pass by memorizing a famous tutorial for this exact API?
2. What would a cheating solution look like (hardcoded answers, empty pass, sleep)?
3. Is the grader gaming-resistant for that cheat?
