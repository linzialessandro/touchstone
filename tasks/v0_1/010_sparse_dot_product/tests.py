from solution import sparse_dot

def assert_close(a, e, msg=""):
    if abs(a - e) > 1e-9:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_close(sparse_dot({0: 1.0, 2: 3.0}, {2: 4.0, 5: 1.0}), 12.0, "basic")
    assert_close(sparse_dot({}, {1: 2.0}), 0.0, "empty")
    assert_close(sparse_dot({1: 0.0, 2: 2.0}, {1: 5.0, 2: 3.0}), 6.0, "zero entry")
    assert_close(sparse_dot({7: -2.0}, {7: -3.0}), 6.0, "neg")
    print("OK")

if __name__ == "__main__":
    main()
