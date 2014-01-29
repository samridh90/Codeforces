#http://codeforces.com/problemset/problem/96/A
def football():
	s = list(raw_input().strip())
	count = 1
	prevChar = s[0]
	for c in s[1:]:
		if c == prevChar:
			count += 1
			if count >= 7:
				return "YES"
		else:
			prevChar = c
			count = 1
	return "NO"

print football()
