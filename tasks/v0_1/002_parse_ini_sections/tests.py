from solution import parse_ini_sections


def assert_eq(actual, expected, msg: str = "") -> None:
    if actual != expected:
        raise AssertionError(f"{msg} expected={expected!r} actual={actual!r}")


def main() -> None:
    text = """
# global comment
[database]
host = localhost
port = 5432

[database]
user = alice

[cache]
; disabled
enabled = true
"""
    got = parse_ini_sections(text)
    assert_eq(
        got,
        {
            "database": {"host": "localhost", "port": "5432", "user": "alice"},
            "cache": {"enabled": "true"},
        },
        "example",
    )

    assert_eq(parse_ini_sections(""), {}, "empty")
    assert_eq(parse_ini_sections("orphan = 1\n"), {}, "pre-section ignored")
    assert_eq(
        parse_ini_sections("[a]\nx = 1\nx = 2\n"),
        {"a": {"x": "2"}},
        "last wins",
    )
    assert_eq(
        parse_ini_sections("[s]\nplain\nk=v=w\n"),
        {"s": {"k": "v=w"}},
        "first equals only",
    )
    print("OK")


if __name__ == "__main__":
    main()
