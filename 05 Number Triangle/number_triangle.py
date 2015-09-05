number = int(raw_input('Enter your number: '))

for i in range(1, number + 1):
	to_show = ''
	for j in range(0, i):
		to_show += str(i)
	print to_show

for i in range(1, number)[::-1]:
	to_show = ''
	for j in range(0, i):
		to_show += str(i)
	print to_show