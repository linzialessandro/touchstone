from concurrent.futures import ThreadPoolExecutor, as_completed

from solution import Counter


def main() -> None:
    c = Counter()
    assert c.value == 0

    n_threads = 32
    per_thread = 500
    expected = n_threads * per_thread

    def worker() -> None:
        for _ in range(per_thread):
            c.increment()

    with ThreadPoolExecutor(max_workers=n_threads) as pool:
        futures = [pool.submit(worker) for _ in range(n_threads)]
        for f in as_completed(futures):
            f.result()

    if c.value != expected:
        raise AssertionError(f"race or logic bug: value={c.value} expected={expected}")
    print("OK")


if __name__ == "__main__":
    main()
