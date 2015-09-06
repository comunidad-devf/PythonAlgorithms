"""Couting Vowels using dictionaries."""

text = raw_input("Give me a text: ").lower()
vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
for letter in text:
    if letter == vowels.keys()[0]:
        vowels['a'] += 1
    elif letter == vowels.keys()[1]:
        vowels['e'] += 1
    elif letter == vowels.keys()[2]:
        vowels['i'] += 1
    elif letter == vowels.keys()[3]:
        vowels['o'] += 1
    elif letter == vowels.keys()[4]:
        vowels['u'] += 1
print "That text has", vowels['a'], "letters a"
print "That text has", vowels['e'], "letters e"
print "That text has", vowels['i'], "letters i"
print "That text has", vowels['o'], "letters o"
print "That text has", vowels['u'], "letters u"
