def get_amazing_perfs(scores):
    mn = scores[0]
    mx = scores[0]
    amzing = 0
    for i in scores[1:]:
        if i < mn:
            mn = i
            amzing += 1
        elif i > mx:
            mx = i
            amzing += 1
    return amzing


if __name__ == '__main__':
    n = int(raw_input())
    scores = map(int, raw_input().strip().split())
    print get_amazing_perfs(scores)
