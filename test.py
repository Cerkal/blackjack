

l = [1, 2, 6, 7, 8, 9, 10]


def straight_test(list):
	count = 0

	for i,x in enumerate(l):
		try:
			if i+1 < len(l):
				if x+1 == l[i+1]:
					count+=1
				else:
					count=0
			if count >= 4:
				return True
		except:
			pass

print(straight_test(l))
