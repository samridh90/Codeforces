from collections import Counter

def beautifulYear():
	y = int(raw_input().strip())
	for i in xrange(y+1, 10000):
		l = len(Counter(str(i)).keys())
		if l == 4:
			return i


print beautifulYear()
