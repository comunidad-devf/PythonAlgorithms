"""Decimal to Binary."""

a = int(raw_input("Give me a number: "))
b = ""
print "Decimal: \t", a
while a > 0:
    b += str(a % 2)
    a = a/2

print "Binary: \t", b[::-1]
