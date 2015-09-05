"""Alphabetical substrings."""

text = raw_input("Give me a text please: ").lower().replace(' ', '') + "_"
ords = [ord(x) for x in text]
last_ord = 0
text = ""
substring = ""
substring_lenght = 0
for number in ords:
    if number > last_ord:
        text += chr(number)
        last_ord = number
    else:
        if len(text) >= substring_lenght:
            substring = text
            substring_lenght = len(text)
        last_ord = 0
        text = ""
        text += chr(number)
print "The last largest substring on that text is:\n", substring
