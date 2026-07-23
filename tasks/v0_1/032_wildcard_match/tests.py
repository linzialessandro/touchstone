from solution import is_match

def assert_eq(a,e,msg=""):
    if a!=e: raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(is_match("adceb", "*a*b"), True, "1")
    assert_eq(is_match("acdcb", "a*c?b"), False, "2")
    assert_eq(is_match("", "*"), True, "empty star")
    assert_eq(is_match("", "?"), False, "empty q")
    assert_eq(is_match("abc", "a*c"), True, "3")
    assert_eq(is_match("abc", "a?c"), True, "4")
    assert_eq(is_match("abc", "a?b"), False, "5")
    print("OK")
if __name__=="__main__":
    main()
