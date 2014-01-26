def coders():
    n = int(raw_input().strip())
    solution = []
    for i in xrange(n):
        inner = []
        f = (i % 2 == 0)
        for j in xrange(n):
            f1 = (j % 2 == 0)
            if f:
                if f1:
                    inner.append("C")
                else:
                    inner.append(".")
            else:
                if f1:
                    inner.append(".")
                else:
                    inner.append("C")
        solution.append(inner)

    print n
    for i in xrange(n):
        print "".join(solution[i])

if __name__ == '__main__':
    coders()
