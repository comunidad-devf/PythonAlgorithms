"""Binary to Decimal."""

a = raw_input("Give me a binary number: ")
powers_of_two = list(reversed([2**x for x in range(len(a))]))
d = 0
for i in range(len(a)):
    d += int(a[i]) * powers_of_two[i]
print "Binary: \t", a
print "Decimal: \t", d
