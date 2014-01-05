def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def epicGame():
    a, b, n = map(int, raw_input().strip().split())
    while True:
        #simon goes first
        if a > n:
            g = gcd(a, n)
        else:
            g = gcd(n, a)
        if n - g < 0:
            return "1"
        else:
            n -= g
        #antisimon goes next
        if b > n:
            g = gcd(b, n)
        else:
            g = gcd(n, b)
        if n - g < 0:
            return "0"
        else:
            n -= g

print epicGame()