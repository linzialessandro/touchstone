from solution import TokenBucket

def main():
    b = TokenBucket(2, 1.0)
    if not b.allow(0.0): raise AssertionError("1")
    if not b.allow(0.0): raise AssertionError("2")
    if b.allow(0.0): raise AssertionError("3")
    if not b.allow(1.0): raise AssertionError("4")
    b2 = TokenBucket(1, 0.0)
    if not b2.allow(0.0): raise AssertionError("5")
    if b2.allow(10.0): raise AssertionError("6 no refill")
    b3 = TokenBucket(5, 2.0)
    if not b3.allow(0.0, 5): raise AssertionError("7")
    if b3.allow(0.5, 2): raise AssertionError("8 only 1 refilled")
    if not b3.allow(1.0, 2): raise AssertionError("9")
    print("OK")
if __name__=="__main__":
    main()
