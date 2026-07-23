def circuit_start(gas: list[int], cost: list[int]) -> int:
    n = len(gas)
    total = tank = 0
    start = 0
    for i in range(n):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 and start < n else -1
