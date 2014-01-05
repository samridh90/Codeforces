def main():
    l = map(int, raw_input().strip().split())
    n, m, a = l[0], l[1], l[2]
    if a == 1:
        return m * n
    n_b = (n % a == 0)
    count_n = n // a
    if not n_b:
        count_n += 1
    if m == n:
        return count_n * count_n
    m_b = (m % a == 0)
    count_m = m // a
    if not m_b:
        count_m += 1

    return count_n * count_m


if __name__ == '__main__':
    print main()
