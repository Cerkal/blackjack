game = True
while game:
	while True:
		x = input('How many starts would you like? ')
		try:
			x = int(x)
		except:
			print('input must be a valid int')
		else:
			break

	line = ''
	for num in range(0,x):
		line+="*"	

	print(line)

	result = input('Would you like more stars? ')
	if (result.lower() != 'y'):
		game = False