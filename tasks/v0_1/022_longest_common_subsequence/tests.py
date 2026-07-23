from solution import lcs_length

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(lcs_length("abcde", "ace"), 3, "basic")
    assert_eq(lcs_length("abc", "def"), 0, "none")
    assert_eq(lcs_length("", "abc"), 0, "empty")
    assert_eq(lcs_length("aaa", "aa"), 2, "repeat")
    assert_eq(lcs_length("AGGTAB", "GXTXAYB"), 4, "classic")
    print("OK")

if __name__ == "__main__":
    main()
