# Syntax reference: kaggle_benchmarks_reference.md
# Touchstone coding task — new slug to avoid stale failed versions.
import kaggle_benchmarks as kbench


@kbench.task(
    name="ts-partition",
    description="Touchstone coding: stable_partition graded by executable asserts.",
)
def ts_partition(llm) -> bool:
    response = llm.prompt(
        "Write a Python function stable_partition(items: list[int], pivot: int) -> list[int] "
        "that returns a new list with all elements < pivot first, then elements >= pivot, "
        "preserving relative order in each part (stable). Do not mutate the input. "
        "Example: [5,1,4,2,3], pivot=3 -> [1,2,5,4,3]. "
        "Return only a python code fence with the full function."
    )
    try:
        code = kbench.tools.python.extract_code(response)
    except Exception:
        return False
    if not code or "stable_partition" not in code:
        return False
    prog = (
        code
        + "\n"
        + "assert stable_partition([5,1,4,2,3], 3) == [1,2,5,4,3]\n"
        + "assert stable_partition([], 0) == []\n"
        + "print('OK')\n"
    )
    try:
        out = kbench.tools.python.script_runner.run_code(prog)
    except Exception:
        return False
    return out.exit_code == 0 and "OK" in (out.stdout or "")


ts_partition.run(kbench.llm)
