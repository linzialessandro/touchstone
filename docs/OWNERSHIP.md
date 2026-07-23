# AI-coding & ownership policy

Locked policy: **D**

| Layer | AI agents | You |
|-------|-----------|-----|
| Glue, docs scaffolding, boilerplate | Allowed | Skim and correct |
| Core: `Task` / `Attempt` / `Grade` / `Run`, grader, runner, lineage | Draft OK | **Must teach every line** |
| Task accept/reject + tests | Draft OK | **You decide** |
| Result claims | — | You must have debugged failures yourself |

## Weekly ownership check

Pick one module at random. With the model **closed**, explain:

1. What invariants it maintains  
2. One failure mode  
3. How a dishonest model output is handled  

## Local drill (no API)

```bash
code-reason grade-file 001_sliding_window_max tasks/v0_1/001_sliding_window_max/reference.py
```

Write a broken solution on purpose and confirm it fails.
