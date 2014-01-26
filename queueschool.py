def get_final_queue(q, t):
    l = len(q) - 1
    for i in xrange(t):
        j = 0
        while j < l:
            if q[j] == 'B' and q[j + 1] == 'G':
                q[j], q[j + 1] = q[j + 1], q[j]
                j += 1
            j += 1
    return q


if __name__ == '__main__':
    n, t = map(int, raw_input().strip().split())
    q = list(raw_input().strip())
    print "".join(map(str, get_final_queue(q, t)))
