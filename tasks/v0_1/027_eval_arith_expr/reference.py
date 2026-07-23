import operator

def eval_expr(expr: str) -> int:
    s = expr.replace(" ", "")
    if not s:
        raise ValueError("empty")
    i = 0
    n = len(s)

    def parse_number():
        nonlocal i
        j = i
        while j < n and s[j].isdigit():
            j += 1
        if j == i:
            raise ValueError("number")
        val = int(s[i:j])
        i = j
        return val

    def parse_factor():
        nonlocal i
        if i < n and s[i] == "(":
            i += 1
            val = parse_expr()
            if i >= n or s[i] != ")":
                raise ValueError("paren")
            i += 1
            return val
        return parse_number()

    def parse_term():
        nonlocal i
        val = parse_factor()
        while i < n and s[i] in "*/":
            op = s[i]
            i += 1
            rhs = parse_factor()
            if op == "*":
                val = val * rhs
            else:
                val = int(val / rhs)
        return val

    def parse_expr():
        nonlocal i
        val = parse_term()
        while i < n and s[i] in "+-":
            op = s[i]
            i += 1
            rhs = parse_term()
            if op == "+":
                val = val + rhs
            else:
                val = val - rhs
        return val

    out = parse_expr()
    if i != n:
        raise ValueError("trailing")
    return out
