from solution import word_wrap

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(word_wrap("hello world ok", 5), ["hello", "world", "ok"], "basic")
    assert_eq(word_wrap("a bb ccc", 6), ["a bb", "ccc"], "pack")
    assert_eq(word_wrap("", 10), [], "empty")
    assert_eq(word_wrap("one", 3), ["one"], "exact")
    try:
        word_wrap("toolong", 3)
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("OK")

if __name__ == "__main__":
    main()
