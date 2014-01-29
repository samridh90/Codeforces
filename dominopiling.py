#http://codeforces.com/problemset/problem/50/A
def dominoPiling():
    m, n = map(int, raw_input().strip().split())
    if not m or not n:
        return 0
    p = m * n
    dominos = p // 2
    return dominos


if __name__ == "__main__":
    print dominoPiling()
