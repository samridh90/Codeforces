#http://codeforces.com/problemset/problem/41/A
def is_translation(a, b):
    return a == b[::-1]


if __name__ == '__main__':
    a = raw_input().strip()
    b = raw_input().strip()
    print "YES" if is_translation(a, b) else "NO"
