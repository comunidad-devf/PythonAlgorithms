"""Couting bobs."""

text = raw_input("Give a bob text: ")
index = text.find('bob')
new_text = text
bobs = 0
while new_text.find('bob') != -1:
    temporal_index = new_text.find('bob')
    new_text = new_text[temporal_index+2:]
    bobs += 1
print "There are", bobs, "bobs in that string"
