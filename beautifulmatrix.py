#http://codeforces.com/problemset/problem/263/A
def beautiful_matrix(n):
    center = (n // 2, n // 2)
    for i in xrange(n):
        l = map(int, raw_input().strip().split())
        try:
            j = l.index(1)
            result = abs(center[0] - i) + abs(center[1] - j)
        except ValueError:
            continue
    return result


if __name__ == '__main__':
    print beautiful_matrix(5)
