from solution import balanced_score


def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")


def main():
    assert_eq(balanced_score("()"), 1, "paren")
    assert_eq(balanced_score("[]"), 2, "bracket")
    assert_eq(balanced_score("([)]"), -1, "cross")
    assert_eq(balanced_score("a(b)c[d]"), 3, "ignore letters")
    assert_eq(balanced_score("(()"), -1, "unclosed")
    assert_eq(balanced_score(""), 0, "empty")
    assert_eq(balanced_score("xyz"), 0, "only noise")
    assert_eq(balanced_score("([]())"), 1 + 2 + 1, "nested")
    assert_eq(balanced_score(")("), -1, "close first")
    assert_eq(balanced_score("([()])"), 1 + 1 + 2, "deep")
    print("OK")


if __name__ == "__main__":
    main()
