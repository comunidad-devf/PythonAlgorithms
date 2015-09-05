"""Couting bobs."""

text = raw_input("Give a bob text: ")
bobs = 0
for i in range(len(text)):
    if text[i: i+3] == 'bob':
        bobs += 1
print "There are", bobs, "bobs in that string"
