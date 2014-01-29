#http://codeforces.com/problemset/problem/158/B
from collections import Counter


def taxi():
	int(raw_input())
	groups = raw_input().strip().split()
	counter = Counter(groups)
	total = 0
	flag_3 = False
	flag_2 = False
	if '4' in counter:
		total += counter['4']
	if '3' in counter:
		total += counter['3']
		flag_3 = True
	if '2' in counter:
		count = counter['2'] // 2
		total += count
		if counter['2'] % 2 != 0:
			if '1' in counter:
				flag_2 = True
			else:
				total += 1
	if '1' in counter:
		count_1 = counter['1']
		if flag_3:
			count_3 = counter['3']
			if count_1 > count_3:
				count_1 -= count_3
			else:
				count_1 = 0
		count = count_1 // 4
		total += count
		rem = count_1 % 4
		if flag_2:
			total += 1
			if rem > 2:
				rem -= 2
			else:
				rem = 0
		if rem != 0:
			total += 1
	return total


if __name__ == '__main__':
	print taxi()
