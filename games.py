from collections import Counter

def host_guest_color():
    n = int(raw_input())
    home = Counter()
    away = Counter()
    for i in xrange(n):
        h, a = map(int, raw_input().strip().split())
        home[h] += 1
        away[a] += 1
    sm = 0
    for key in home.keys():
        t = home[key] * away[key]
        sm += t
    return sm


if __name__ == '__main__':
    print host_guest_color()
