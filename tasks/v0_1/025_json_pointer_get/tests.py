from solution import pointer_get

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    doc = {"a": [{"b": 2}, 3], "x": {"y": [10]}}
    assert_eq(pointer_get(doc, ""), doc, "root")
    assert_eq(pointer_get(doc, "/a/0/b"), 2, "nested")
    assert_eq(pointer_get(doc, "/a/1"), 3, "list val")
    assert_eq(pointer_get(doc, "/x/y/0"), 10, "deep")
    try:
        pointer_get(doc, "/a/5")
        raise AssertionError("expected KeyError")
    except KeyError:
        pass
    try:
        pointer_get(doc, "/missing")
        raise AssertionError("expected KeyError")
    except KeyError:
        pass
    try:
        pointer_get(doc, "/a/00")
        raise AssertionError("expected KeyError for leading zero")
    except KeyError:
        pass
    print("OK")

if __name__ == "__main__":
    main()
