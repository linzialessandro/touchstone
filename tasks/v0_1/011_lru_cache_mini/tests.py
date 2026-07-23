from solution import LRUCache

def main():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    if c.get(1) != 1:
        raise AssertionError("get1")
    c.put(3, 3)
    if c.get(2) != -1:
        raise AssertionError("evicted 2")
    if c.get(3) != 3:
        raise AssertionError("get3")
    c.put(4, 4)
    if c.get(1) != -1:
        raise AssertionError("evicted 1")
    if c.get(3) != 3 or c.get(4) != 4:
        raise AssertionError("remaining")
    c.put(3, 30)
    if c.get(3) != 30:
        raise AssertionError("update")
    print("OK")

if __name__ == "__main__":
    main()
