"""Couting Vowels using dictionaries."""

text = raw_input("Give a text: ")
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
print "We haver", vowels['a'], "letters a"
print "We haver", vowels['e'], "letters e"
print "We haver", vowels['i'], "letters i"
print "We haver", vowels['o'], "letters o"
print "We haver", vowels['u'], "letters u"
