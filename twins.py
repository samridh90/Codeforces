#http://codeforces.com/problemset/problem/160/A
def twinCoins():
	int(raw_input())
	l = map(int, raw_input().strip().split())
	s1 = sum(l)
	s2 = 0
	count = 0
	l.sort(reverse=True)
	for e in l:
		s2 += e
		s1 -= e
		count += 1
		if s2 > s1:
			return count


print twinCoins()
