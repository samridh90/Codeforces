def capsLock():
	s = raw_input().strip()
	if s.isupper():
		return s.lower()
	elif s[0].islower() and (not s[1:] or s[1:].isupper()):
		return s.capitalize()
	else:
		return s

print capsLock()