"""Counting vowels, each one."""
text = raw_input("Give a text: ")
a = 0
e = 0
i = 0
o = 0
u = 0
for letter in text:
    if letter == 'a':
        a += 1
    elif letter == 'e':
        e += 1
    elif letter == 'i':
        i += 1
    elif letter == 'o':
        o += 1
    elif letter == 'u':
        u += 1
print "We haver", a, "letters a"
print "We haver", e, "letters e"
print "We haver", i, "letters i"
print "We haver", o, "letters o"
print "We haver", u, "letters u"
