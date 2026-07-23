from solution import circuit_start

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(circuit_start([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3, "classic")
    assert_eq(circuit_start([2, 3, 4], [3, 4, 3]), -1, "impossible")
    assert_eq(circuit_start([5], [4]), 0, "single")
    assert_eq(circuit_start([2, 0, 0], [0, 1, 0]), 0, "small")
    print("OK")

if __name__ == "__main__":
    main()
