string = ''.join(sorted(raw_input().lower().replace(' ', '')))
single = 0
while len(string) > 0:
    letter = string[0]
    if string.count(letter) %2 != 0:
        single += 1
    if single > 1:
        print "NO"
        break
    string = string.replace(letter, '')

if single <= 1:
    print "YES"
