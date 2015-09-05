"""Number Pyramids."""

n = int(raw_input("Give me a number: "))
numbers = range(1, n+1) + range(1, n+1)[::-1]
for number in numbers:
    print str(number) * number
