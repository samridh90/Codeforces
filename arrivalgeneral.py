#http://codeforces.com/problemset/problem/144/A
def get_max_index(lst):
    l = len(lst) - 1
    m = max(lst)
    idx = l
    while l >= 0:
        if lst[l] == m:
            idx = l
        l -= 1
    return idx


def get_min_index(lst):
    l = len(lst)
    m = min(lst)
    i = 0
    idx = 0
    while i < l:
        if lst[i] == m:
            idx = i
        i += 1
    return idx


def get_time_to_swap(lst):
    max_idx = get_max_index(lst)
    min_idx = get_min_index(lst)
    l = len(lst)
    res = max_idx + (l - min_idx - 1)
    if min_idx < max_idx:
        return res - 1
    else:
        return res


if __name__ == '__main__':
    n = int(raw_input())
    lst = map(int, raw_input().strip().split())
    print get_time_to_swap(lst)
