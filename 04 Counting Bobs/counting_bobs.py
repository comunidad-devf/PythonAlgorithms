"""Couting bobs."""

text = raw_input("Give me a bob text: ").lower()
bobs = 0
for i in range(len(text)):
    if text[i: i+3] == 'bob':
        bobs += 1
print "There are", bobs, "bobs in that string"
