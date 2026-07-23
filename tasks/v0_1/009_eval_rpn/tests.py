from solution import eval_rpn

def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(eval_rpn(["2", "1", "+", "3", "*"]), 9, "basic")
    assert_eq(eval_rpn(["4", "13", "5", "/", "+"]), 6, "div")
    assert_eq(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22, "long")
    assert_eq(eval_rpn(["7", "-3", "/"]), -2, "toward zero")
    assert_eq(eval_rpn(["3"]), 3, "single")
    try:
        eval_rpn([])
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("OK")

if __name__ == "__main__":
    main()
