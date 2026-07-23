from solution import stable_partition

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    src = [5, 1, 4, 2, 3]
    assert_eq(stable_partition(src, 3), [1, 2, 5, 4, 3], "basic")
    if src != [5, 1, 4, 2, 3]:
        raise AssertionError("mutated")
    assert_eq(stable_partition([], 0), [], "empty")
    assert_eq(stable_partition([1, 2, 3], 0), [1, 2, 3], "all ge")
    assert_eq(stable_partition([1, 2, 3], 9), [1, 2, 3], "all lt")
    print("OK")

if __name__ == "__main__":
    main()
