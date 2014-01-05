def doubleCola():
    n = long(raw_input().strip())
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    if n <= 5:
        return names[n - 1]
    p = 1
    while(True):
        s = 5 * p
        if s > n:
            break
        n = n - s
        p = p << 1
    return names[n // p]

print doubleCola()
