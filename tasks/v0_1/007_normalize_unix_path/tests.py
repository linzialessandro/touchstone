from solution import normalize_path

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(normalize_path("/a/./b/../c/"), "/a/c", "basic abs")
    assert_eq(normalize_path("a/b/../../c"), "c", "rel collapse")
    assert_eq(normalize_path(""), ".", "empty")
    assert_eq(normalize_path("."), ".", "dot")
    assert_eq(normalize_path("/../a"), "/a", "abs root parent ignored")
    assert_eq(normalize_path("../a/b"), "../a/b", "rel parent kept")
    assert_eq(normalize_path("///a////b"), "/a/b", "slashes")
    assert_eq(normalize_path("/"), "/", "root")
    print("OK")

if __name__ == "__main__":
    main()
