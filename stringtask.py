#http://codeforces.com/problemset/problem/118/A
def modifyString():
	src = list(raw_input().strip())
	vowels = {"A":True, "O":True, "Y":True, "E":True, "U":True, "I":True}
	res = ""
	for c in src:
		if c.upper() in vowels:
			continue
		else:
			res += "." + c.lower()
	print res


if __name__ == '__main__':
	modifyString()
