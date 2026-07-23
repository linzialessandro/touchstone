"""Executable grader tests for 001_sliding_window_max."""

from solution import max_sliding_window


def assert_eq(actual, expected, msg: str = "") -> None:
    if actual != expected:
        raise AssertionError(f"{msg} expected={expected!r} actual={actual!r}")


def main() -> None:
    assert_eq(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7], "classic")
    assert_eq(max_sliding_window([1], 1), [1], "single")
    assert_eq(max_sliding_window([9, 8, 7, 6], 2), [9, 8, 7], "decreasing")
    assert_eq(max_sliding_window([1, 2, 3], 0), [], "k=0")
    assert_eq(max_sliding_window([], 3), [], "empty")
    assert_eq(max_sliding_window([1, 2, 3], 5), [], "k too large")
    assert_eq(max_sliding_window([-1, -2, -3, -4], 2), [-1, -2, -3], "negatives")
    # Hidden-ish case: plateaus
    assert_eq(max_sliding_window([2, 2, 2, 2], 3), [2, 2], "plateau")
    print("OK")


if __name__ == "__main__":
    main()
