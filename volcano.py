from collections import deque


def volcano():
    n, m = map(long, raw_input().strip().split())
    volcano = {}
    for i in xrange(m):
        r, s = map(long, raw_input().strip().split())
        volcano[(r,s)] = True
    q = deque()
    prev = {}
    start = (1, 1)
    end = (n, n)
    if start == end:
        return 0
    q.append(start)
    flag = False
    while len(q) > 0:
        p = q.popleft()
        if p == end:
            flag = True
            break
        n1 = (p[0] + 1, p[1])
        n2 = (p[0], p[1] + 1)
        if n1 not in volcano:
            prev[n1] = p
            q.append(n1)
        if n2 not in volcano:
            prev[n2] = p
            q.append(n2)
    if flag:
        time = 1
        cur = prev[end]
        while cur != start:
            time += 1
            cur = prev[cur]

        return time
    else:
        return -1

print volcano()
