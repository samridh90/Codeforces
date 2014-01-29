#http://codeforces.com/problemset/problem/112/A
def hq9():
	s = list(raw_input().strip())
	d = {'H': True, 'Q': True, '9': True}
	for c in s:
		if c in d:
			return "YES"
	return "NO"

print hq9()
