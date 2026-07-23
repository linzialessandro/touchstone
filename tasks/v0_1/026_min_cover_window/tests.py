from solution import min_cover_window

def assert_eq(a,e,msg=""):
    if a!=e: raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(min_cover_window("ADOBECODEBANC", {"A":1,"B":1,"C":1}), "BANC", "classic")
    assert_eq(min_cover_window("a", {"a":1}), "a", "single")
    assert_eq(min_cover_window("a", {"a":2}), "", "impossible")
    assert_eq(min_cover_window("aa", {"a":2}), "aa", "dup need")
    assert_eq(min_cover_window("xyz", {}), "", "empty need")
    assert_eq(min_cover_window("abdecfab", {"a":1,"b":1,"c":1}), "cfab", "leftmost shortest? ")
    # shortest length 3: "decf"? has d,e,c,f - need a,b,c - "cfab" len 4; "abdecfab"
    # windows with a,b,c: "abdec" has a,b,c? a,b,d,e,c yes len5; "bdecf" no a; "decfab" has c,f,a,b len6; "cfab" len4; "ab" at start no c
    # "abdecfab" - positions: actually "fab" has no c. "cfab" is correct length 4
    # is there length 3? cab at end - c,f,a,b - no 3-char with a,b,c consecutive multiset
    # "bdecfa" no. OK
    print("OK")
if __name__=="__main__":
    main()
