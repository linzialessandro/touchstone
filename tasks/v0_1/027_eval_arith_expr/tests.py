from solution import eval_expr

def assert_eq(a,e,msg=""):
    if a!=e: raise AssertionError(f"{msg} expected={e!r} actual={a!r}")

def main():
    assert_eq(eval_expr("3+2*2"), 7, "prec")
    assert_eq(eval_expr("(1+(4+5+2)-3)+(6+8)"), 23, "parens")
    assert_eq(eval_expr(" 3+5 / 2 "), 5, "div toward zero")
    assert_eq(eval_expr("14-3*2"), 8, "sub")
    assert_eq(eval_expr("2*(3+4)"), 14, "mul paren")
    try:
        eval_expr("")
        raise AssertionError("empty")
    except ValueError:
        pass
    print("OK")
if __name__=="__main__":
    main()
