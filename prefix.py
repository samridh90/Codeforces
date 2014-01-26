def prefix():
    m = long(raw_input().strip())
    s = []
    for i in xrange(m):
        inpt = map(long, raw_input().strip().split())
        if inpt[0] == 1:
            s.append(inpt[1])
        else:
            l = inpt[1]
            t = inpt[2]
            s += (s[:l] * t)
    n = long(raw_input().strip())
    ls = map(long, raw_input().strip().split())
    for i in ls:
        print s[i-1],


prefix()
