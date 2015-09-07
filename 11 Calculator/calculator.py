"""Python Calculator."""


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def modulus(a, b):
    return a % b


def compare(a, b):
    if a > b:
        return str(a) + " is grather than " + str(b)
    else:
        return str(b) + " is grather than " + str(a)

print "\n\t\t_____Python Calculator_____\n"
print "Which operation below do you want to perform?"
print "\t1. Add"
print "\t2. Substract"
print "\t3. Multiply"
print "\t4. Divide"
print "\t5. Modulus"
print "\t6. Compare"
o = raw_input()

print "\nOk, enter two numbers:"
a = float(raw_input("a: "))
b = float(raw_input("b: "))

if o == '1':
    print add(a, b)
elif o == '2':
    print substract(a, b)
elif o == '3':
    print multiply(a, b)
elif o == '4':
    print divide(a, b)
elif o == '5':
    print modulus(a, b)
elif o == '6':
    print compare(a, b)
else:
    print "Invalid option"
