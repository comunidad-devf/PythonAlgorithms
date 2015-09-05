"""Counting Vowels."""

text = raw_input("Give a string plz\n")

vowels = 'aeiou'
count = 0
for letter in text:
    if letter in vowels:
        count += 1

print 'There are', count, 'vowels in', text
