#http://codeforces.com/problemset/problem/339/A
from collections import Counter

def helpfulMath():
	c = Counter(raw_input().strip())
	ones = ["1" for i in xrange(c['1'])]
	twos = ["2" for i in xrange(c['2'])]
	threes = ["3" for i in xrange(c['3'])]
	res = ""
	if ones:
		res += "+".join(ones)
	if twos:
		if res:
			res += "+" + "+".join(twos)
		else:
			res += "+".join(twos)
	if threes:
		if res:
			res += "+" + "+".join(threes)
		else:
			res += "+".join(threes)
	return res

print helpfulMath()
