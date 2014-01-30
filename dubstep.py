#http://codeforces.com/problemset/problem/208/A
def get_original_string(s):
    dub = "WUB"
    res = s.split(dub)
    res_str = " ".join([r for r in res if r != ""])
    return res_str


if __name__ == '__main__':
    s = raw_input().strip()
    print get_original_string(s)
