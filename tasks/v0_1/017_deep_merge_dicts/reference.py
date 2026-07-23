def deep_merge(a: dict, b: dict) -> dict:
    out = dict(a)
    for k, bv in b.items():
        if k not in out:
            out[k] = bv
            continue
        av = out[k]
        if isinstance(av, dict) and isinstance(bv, dict):
            out[k] = deep_merge(av, bv)
        elif isinstance(av, list) and isinstance(bv, list):
            out[k] = av + bv
        else:
            out[k] = bv
    return out
