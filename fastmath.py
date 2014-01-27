def get_diff(a, b):
    res = []
    for i, j in zip(a, b):
        res.append(i ^ j)
    return res


if __name__ == '__main__':
    a = map(int, list(raw_input().strip()))
    b = map(int, list(raw_input().strip()))
    print "".join(map(str, get_diff(a, b)))

