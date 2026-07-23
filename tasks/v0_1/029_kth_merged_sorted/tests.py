from solution import kth_sorted

def assert_eq(a,e,msg=""):
    if a!=e: raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(kth_sorted([1,3,5],[2,4,6],4), 4, "basic")
    assert_eq(kth_sorted([1,2,3],[],2), 2, "one empty")
    assert_eq(kth_sorted([],[7],1), 7, "other empty")
    assert_eq(kth_sorted([1,1,1],[1],3), 1, "dups")
    try:
        kth_sorted([1],[2],0)
        raise AssertionError("range")
    except IndexError:
        pass
    try:
        kth_sorted([1],[2],4)
        raise AssertionError("range2")
    except IndexError:
        pass
    print("OK")
if __name__=="__main__":
    main()
