#http://codeforces.com/problemset/problem/387/A
def get_time(t1, t2):
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))
    m_diff = m1 - m2
    h_diff = h1 - h2
    if m_diff < 0:
        m_diff += 60
        h_diff -= 1
    if h_diff < 0:
        h_diff += 24
    res = ""
    if h_diff < 10:
        res += ("0" + str(h_diff))
    else:
        res += str(h_diff)
    res += ":"
    if m_diff < 10:
        res += ("0" + str(m_diff))
    else:
        res += str(m_diff)
    return res

if __name__ == '__main__':
    t1 = raw_input().strip()
    t2 = raw_input().strip()
    print get_time(t1, t2)
