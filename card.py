def card():
    n = int(raw_input().strip())
    l = map(int, raw_input().strip().split())
    sum1, sum2 = 0, 0
    f, b = 0, len(l) - 1
    t = 0
    while f <= b:
        if t % 2 == 0:
            if l[f] > l[b]:
                sum1 += l[f]
                f += 1
            else:
                sum1 += l[b]
                b -= 1
        else:
            if l[f] > l[b]:
                sum2 += l[f]
                f += 1
            else:
                sum2 += l[b]
                b -= 1
        t += 1
    return sum1, sum2


c = card()
print c[0], c[1]
