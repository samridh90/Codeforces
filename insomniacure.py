def dragonDamage():
    k = int(raw_input().strip())
    l = int(raw_input().strip())
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    d = int(raw_input().strip())
    t = [True for i in xrange(d)]
    for i in xrange(d):
        j = i + 1
        if j % k == 0 or j % l == 0 or j % m == 0 or j % n == 0:
            t[i] = False
    return t.count(False)

print dragonDamage()
