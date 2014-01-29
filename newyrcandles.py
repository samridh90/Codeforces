#http://codeforces.com/problemset/problem/379/A
def get_number_of_candles(a, b):
    res = a
    rem = 0
    while a > 0:
        a += rem
        s = a // b
        res += s
        rem = a % b
        a = s
    return res


if __name__ == '__main__':
    a, b = map(int, raw_input().strip().split())
    print get_number_of_candles(a, b)
