from solution import merge_labeled


def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")


def main():
    assert_eq(
        merge_labeled([(1, 3, "a"), (2, 5, "a"), (4, 6, "b")]),
        [(1, 5, "a"), (4, 6, "b")],
        "basic",
    )
    assert_eq(merge_labeled([]), [], "empty")
    assert_eq(merge_labeled([(5, 1, "x")]), [], "invalid dropped")
    assert_eq(
        merge_labeled([(1, 2, "a"), (3, 4, "a")]),
        [(1, 4, "a")],
        "touching",
    )
    assert_eq(
        merge_labeled([(1, 10, "a"), (2, 3, "b"), (4, 5, "a")]),
        [(1, 10, "a"), (2, 3, "b")],
        "nested different labels; a merges across",
    )
    # (1,10,a) and (4,5,a) merge to (1,10,a)
    assert_eq(
        merge_labeled([(1, 2, "b"), (1, 2, "a")]),
        [(1, 2, "a"), (1, 2, "b")],
        "sort by label after start/end",
    )
    print("OK")


if __name__ == "__main__":
    main()
