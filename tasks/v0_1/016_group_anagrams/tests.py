from solution import group_anagrams

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        "classic",
    )
    assert_eq(group_anagrams([]), [], "empty")
    assert_eq(group_anagrams([""]), [[""]], "empty word")
    assert_eq(group_anagrams(["a", "b", "a"]), [["a", "a"], ["b"]], "dup")
    print("OK")

if __name__ == "__main__":
    main()
