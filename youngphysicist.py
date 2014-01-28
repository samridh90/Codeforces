def is_in_equilibrium(v, n):
    s1 = 0
    s2 = 0
    s3 = 0
    for i in xrange(n):
        j = v[i]
        s1 += j[0]
        s2 += j[1]
        s3 += j[2]
    return s1 == 0 and s2 ==0 and s3 == 0

if __name__ == '__main__':
    n = int(raw_input())
    ip = []
    for i in xrange(n):
        j = map(int, raw_input().strip().split())
        ip.append(j)
    print "YES" if is_in_equilibrium(ip, n) else "NO"
