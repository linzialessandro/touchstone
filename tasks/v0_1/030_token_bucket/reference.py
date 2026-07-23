class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float) -> None:
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.t = None

    def allow(self, timestamp: float, tokens: int = 1) -> bool:
        if self.t is None:
            self.t = timestamp
            self.tokens = float(self.capacity)
        else:
            dt = timestamp - self.t
            if dt < 0:
                raise ValueError("time")
            self.tokens = min(self.capacity, self.tokens + dt * self.refill_rate)
            self.t = timestamp
        if tokens <= self.tokens:
            self.tokens -= tokens
            return True
        return False
