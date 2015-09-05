"""Alphabetical substrings."""

text = raw_input("Give me a text plz: ")
substring = ""
last_ord = 0
max_substring_l = 0
max_substring = ""
for letter in text.lower():
    if ord(letter) > last_ord:
        substring += letter
        last_ord = ord(letter)
    else:
        substring = ""
        last_ord = 0
print substring
