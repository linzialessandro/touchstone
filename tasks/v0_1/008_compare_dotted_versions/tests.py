from solution import cmp_version

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(cmp_version("1.2", "1.2.0"), 0, "pad")
    assert_eq(cmp_version("1.10", "1.2"), 1, "ten vs two")
    assert_eq(cmp_version("0.1", "1.0"), -1, "minor")
    assert_eq(cmp_version("2", "2.0.0.0"), 0, "pad long")
    assert_eq(cmp_version("1.0.1", "1.0.0"), 1, "patch")
    try:
        cmp_version("1..2", "1.0")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    try:
        cmp_version("1.a", "1.0")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("OK")

if __name__ == "__main__":
    main()
