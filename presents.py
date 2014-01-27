def get_presents(p):
    l = len(p)
    res = [0] * l
    for i, v in enumerate(p):
        res[v - 1] = i + 1
    return res


if __name__ == '__main__':
    n = int(raw_input())
    p = map(int, raw_input().strip().split())
    res = get_presents(p)
    print " ".join(map(str, res))
