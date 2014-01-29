#http://codeforces.com/problemset/problem/266/A
def stones():
	n = int(raw_input().strip())
	s = list(raw_input().strip())
	lastChr = s[0]
	count = 0
	for c in s[1:]:
		if c == lastChr:
			count += 1
		lastChr = c
	return count

print stones()
