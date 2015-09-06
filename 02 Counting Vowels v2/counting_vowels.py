"""Counting vowels, each one."""
text = raw_input("Give me a text: ").lower()
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
print "That text has", a, "letters a"
print "That text has", e, "letters e"
print "That text has", i, "letters i"
print "That text has", o, "letters o"
print "That text has", u, "letters u"
