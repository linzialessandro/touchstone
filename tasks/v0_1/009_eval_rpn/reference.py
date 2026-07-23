import operator

def eval_rpn(tokens: list[str]) -> int:
    if not tokens:
        raise ValueError("empty")
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b),  # toward zero
    }
    stack: list[int] = []
    for t in tokens:
        if t in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack[-1]
