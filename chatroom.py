#http://codeforces.com/problemset/problem/58/A
def said_hello(t):
    s = "hello"
    i = 0
    for char in t:
        if char == s[i]:
            i += 1
        if i == len(s):
            return True
    return False


if __name__ == '__main__':
    t = raw_input().strip()
    print "YES" if said_hello(t) else "NO"
