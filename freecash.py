#http://codeforces.com/problemset/problem/237/A
from collections import Counter


def free_cash_reg():
    n = int(raw_input().strip())
    c = Counter()
    for i in xrange(n):
        ip = raw_input().strip()
        c[ip] += 1
    return c.most_common()[0][1]


if __name__ == '__main__':
    print free_cash_reg()
