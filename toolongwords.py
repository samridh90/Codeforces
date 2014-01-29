#http://codeforces.com/problemset/problem/71/A
def abbrWord():
	n = int(raw_input())
	for i in xrange(n):
		src = raw_input().strip()
		l = len(src)
		if l <= 10:
			print src
		else:
			res = "%s%d%s" % (src[0], l - 2, src[l-1])
			print res


if __name__ == '__main__':
	abbrWord()
