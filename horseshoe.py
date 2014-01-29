#http://codeforces.com/problemset/problem/228/A
from collections import Counter

def horseShoe():
	c = Counter(raw_input().strip().split())
	l = len(c.keys())
	d = 4 - l
	return d

print horseShoe()
