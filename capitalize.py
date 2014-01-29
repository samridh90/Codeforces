#http://codeforces.com/problemset/problem/281/A
def capitalize():
	s = raw_input().strip()
	if not s[0].isupper():
		s = s[0].upper() + s[1:]
	return s


print capitalize()
