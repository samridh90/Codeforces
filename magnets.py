#http://codeforces.com/problemset/problem/344/A
def get_num_groups(l):
    cur = l[0]
    numGroups = 1
    for m in l[1:]:
        if m != cur:
            cur = m
            numGroups += 1
    return numGroups


if __name__ == '__main__':
    n = int(raw_input())
    ip = []
    for i in xrange(n):
        ip.append(raw_input().strip())
    print get_num_groups(ip)
