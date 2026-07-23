from solution import project_rows


def assert_eq(a, e, msg=""):
    if a != e:
        raise AssertionError(f"{msg} expected={e!r} actual={a!r}")


def main():
    text = """name,age,city
ann,30,rome
bob,badrow
cara,25,milan
"""
    assert_eq(
        project_rows(text, ["city", "name"]),
        [{"city": "rome", "name": "ann"}, {"city": "milan", "name": "cara"}],
        "example",
    )
    assert_eq(project_rows("", ["a"]), [], "empty")
    assert_eq(project_rows("h1,h2\n1,2,3\n", ["h1"]), [], "all bad rows")
    assert_eq(
        project_rows("a,b\n1,2\n", ["b", "z"]),
        [{"b": "2"}],
        "unknown column ignored",
    )
    assert_eq(
        project_rows("  x , y  \n  3 , 4  \n", ["x"]),
        [{"x": "3"}],
        "strip spaces",
    )
    print("OK")


if __name__ == "__main__":
    main()
