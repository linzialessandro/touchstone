def stable_partition(items: list[int], pivot: int) -> list[int]:
    left = [x for x in items if x < pivot]
    right = [x for x in items if x >= pivot]
    return left + right
