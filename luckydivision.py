def is_lucky(n):
    s = str(n)
    lucky_digits = {'4': True, '7': True}
    for char in s:
        if char not in lucky_digits:
            return False
    return True


def is_almost_lucky(n):
    if is_lucky(n):
        return True
    for i in xrange(n):
        if is_lucky(i) and n % i == 0:
            return True
    return False


if __name__ == '__main__':
    n = int(raw_input())
    print "YES" if is_almost_lucky(n) else "NO"

