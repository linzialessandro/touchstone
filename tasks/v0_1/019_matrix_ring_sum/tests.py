from solution import ring_sum

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert_eq(ring_sum(m, 0), 40, "outer")
    assert_eq(ring_sum(m, 1), 5, "inner")
    assert_eq(ring_sum(m, 2), 0, "missing")
    assert_eq(ring_sum([[7]], 0), 7, "1x1")
    assert_eq(ring_sum([[1, 2, 3]], 0), 6, "row")
    assert_eq(ring_sum([[1], [2], [3]], 0), 6, "col")
    print("OK")

if __name__ == "__main__":
    main()
