def stringGame():
	s1 = list(raw_input().strip().lower())
	s2 = list(raw_input().strip().lower())
	if s1 == s2:
		return '0'
	for a, b in zip(s1, s2):
		if a < b:
			return '-1'
		elif b < a:
			return '1'


print stringGame()