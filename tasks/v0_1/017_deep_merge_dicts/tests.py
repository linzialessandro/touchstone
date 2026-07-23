from solution import deep_merge

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    a = {"x": 1, "d": {"y": 2}, "k": [1]}
    b = {"x": 9, "d": {"z": 3}, "k": [2]}
    out = deep_merge(a, b)
    assert_eq(out, {"x": 9, "d": {"y": 2, "z": 3}, "k": [1, 2]}, "basic")
    if a["k"] != [1] or b["k"] != [2]:
        raise AssertionError("mutated inputs")
    assert_eq(deep_merge({}, {"a": 1}), {"a": 1}, "empty a")
    assert_eq(deep_merge({"a": {"b": 1}}, {"a": 2}), {"a": 2}, "overwrite dict with scalar")
    print("OK")

if __name__ == "__main__":
    main()
