from solution import rle_encode

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(rle_encode("AABCCC"), "A2BC3", "basic")
    assert_eq(rle_encode("WWWWB"), "W4B", "w")
    assert_eq(rle_encode("ABC"), "ABC", "singles")
    assert_eq(rle_encode(""), "", "empty")
    assert_eq(rle_encode("AAAA"), "A4", "four")
    try:
        rle_encode("ABa")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("OK")

if __name__ == "__main__":
    main()
