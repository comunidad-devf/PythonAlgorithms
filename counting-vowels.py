s = raw_input("Give a string plz\n")

vowels = 'aeiou'
count = 0
for char in s:
	if (char in vowels):
		count += 1
		continue

print 'Number of vowels in', s, ': ', str(count)