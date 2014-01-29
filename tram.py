#http://codeforces.com/contest/116/submission/5608892
def tramCapacity():
    n = int(raw_input().strip())
    pout, pin = map(int, raw_input().strip().split())
    sm = pin
    mx = pin
    for i in xrange(n-1):
        pout, pin = map(int, raw_input().strip().split())
        sm = sm - pout + pin
        if sm > mx:
            mx = sm
    return mx


if __name__ == "__main__":
    print tramCapacity()
