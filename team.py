#http://codeforces.com/problemset/problem/231/A
def team():
    n = int(raw_input().strip())
    count = 0
    for i in xrange(n):
        vec = map(int, raw_input().strip().split())
        s = sum(vec)
        if s >= 2:
            count += 1
    return count

if __name__ == "__main__":
    print team()
