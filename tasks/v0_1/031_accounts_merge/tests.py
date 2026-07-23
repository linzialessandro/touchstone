from solution import merge_accounts

def assert_eq(a,e,msg=""):
    if a!=e: raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    acc = [
        ["John", "j@x", "j@y"],
        ["John", "j@y", "j@z"],
        ["Mary", "m@x"],
    ]
    assert_eq(
        merge_accounts(acc),
        [["John", "j@x", "j@y", "j@z"], ["Mary", "m@x"]],
        "basic",
    )
    assert_eq(merge_accounts([["A", "a@a"]]), [["A", "a@a"]], "single")
    acc2 = [
        ["John", "a", "b"],
        ["John", "c"],
        ["John", "b", "d"],
    ]
    assert_eq(
        merge_accounts(acc2),
        [["John", "a", "b", "d"], ["John", "c"]],
        "partial",
    )
    print("OK")
if __name__=="__main__":
    main()
