from collections import Counter

def boyOrGirl():
	s = raw_input().strip()
	c = Counter(s)
	l = len(c.keys())
	if l % 2 == 0:
		return "CHAT WITH HER!"
	else:
		return "IGNORE HIM!"


print boyOrGirl()