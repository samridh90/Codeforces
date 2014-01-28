def get_button_presses(n):
    s1 = n
    s2 = (n * (n - 1) * n) // 2
    s3 = ((n - 1) * n * (2 * n - 1)) // 6
    return s1 + s2 - s3


if __name__ == '__main__':
    n = int(raw_input())
    print get_button_presses(n)
