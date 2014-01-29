#http://codeforces.com/problemset/problem/282/A
def bitplusplus():
	n = int(raw_input().strip())
	x = 0
	plusOp1 = "X++"
	plusOp2 = "++X"
	minusOp1 = "X--"
	minusOp2 = "--X"
	for i in xrange(n):
		op = raw_input().strip()
		if op.startswith(plusOp1) or op.startswith(plusOp2):
			x += 1
		elif op.startswith(minusOp1) or op.startswith(minusOp2):
			x -= 1
	return x

print bitplusplus()
