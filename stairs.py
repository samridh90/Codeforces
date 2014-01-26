from heapq import heappush, heappop, heapify
from collections import deque
def stairs():
    m = long(raw_input().strip())
    cards = map(int, raw_input().strip().split())
    l = len(cards)
    cards = [-c for c in cards]
    heapify(cards)
    seq = deque()
    mx = -1 * heappop(cards)
    seq.append(mx)
    r_flag = False
    for i in xrange(l - 1):
        p = heappop(cards) * -1
        if p < seq[-1]:
            seq.append(p)
            r_flag = False
        elif p > seq[-1]:
            seq.appendleft(p)
            r_flag = False
        elif p == seq[-1]  and p != mx and not r_flag:
            seq.appendleft(p)
            r_flag = True
    return seq

s = stairs()
print len(s)
print " ".join(map(str, s))
