from solution import topo_sort

def is_valid(n, edges, order):
    if order == []:
        return True  # caller checks cycle cases separately when needed
    if sorted(order) != list(range(n)):
        return False
    pos = {node: i for i, node in enumerate(order)}
    return all(pos[u] < pos[v] for u, v in edges)

def main():
    edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
    order = topo_sort(4, edges)
    if not is_valid(4, edges, order) or order == []:
        raise AssertionError(f"bad order {order}")
    if topo_sort(2, [(0, 1), (1, 0)]) != []:
        raise AssertionError("cycle")
    if topo_sort(1, []) != [0]:
        raise AssertionError("single")
    if topo_sort(3, []) not in ([0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]):
        # any permutation of independent nodes
        o = topo_sort(3, [])
        if sorted(o) != [0, 1, 2]:
            raise AssertionError(f"independent {o}")
    print("OK")

if __name__ == "__main__":
    main()
