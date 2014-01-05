from collections import Counter

def lucky():
	n = list(raw_input().strip())
	c = Counter(n)
	count = c['4'] + c['7']
	if count == 4 or count == 7:
		return "YES"
	return "NO"

print lucky()