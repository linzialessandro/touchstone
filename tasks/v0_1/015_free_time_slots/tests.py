from solution import free_slots

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(
        free_slots([(1, 3), (2, 4), (7, 8)], 0, 10),
        [(0, 1), (4, 7), (8, 10)],
        "basic",
    )
    assert_eq(free_slots([], 0, 5), [(0, 5)], "all free")
    assert_eq(free_slots([(0, 5)], 0, 5), [], "all busy")
    assert_eq(free_slots([( -2, 2), (8, 20)], 0, 10), [(2, 8)], "clip")
    assert_eq(free_slots([(1, 1), (3, 2)], 0, 4), [(0, 4)], "invalid busy")
    assert_eq(free_slots([], 5, 5), [], "empty day")
    print("OK")

if __name__ == "__main__":
    main()
