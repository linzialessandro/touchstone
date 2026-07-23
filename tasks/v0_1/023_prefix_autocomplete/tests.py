from solution import autocomplete

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    words = ["apple", "app", "application", "banana"]
    assert_eq(autocomplete(words, "app", 2), ["app", "apple"], "basic")
    assert_eq(autocomplete(words, "ban", 5), ["banana"], "one")
    assert_eq(autocomplete(words, "z", 3), [], "none")
    assert_eq(autocomplete(words, "app", 0), [], "k0")
    assert_eq(autocomplete(["b", "a", "a"], "a", 5), ["a", "a"], "dups")
    print("OK")

if __name__ == "__main__":
    main()
