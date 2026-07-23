from solution import coverage_length

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(coverage_length([(1, 4), (3, 6), (8, 9)]), 6, "basic")
    assert_eq(coverage_length([]), 0, "empty")
    assert_eq(coverage_length([(5, 5), (3, 1)]), 0, "invalid")
    assert_eq(coverage_length([(0, 10), (2, 3)]), 10, "nested")
    assert_eq(coverage_length([(1, 2), (2, 3)]), 2, "touching")
    print("OK")

if __name__ == "__main__":
    main()
