s = 'asdfjasdfjasofjasodfjaobobasdfkasodfsadfakjvbasbivoasdvboasbvosadbobasdi'
word = 'bob'
found = 0
word_len = len('bob')
s_len = len(s)
found_at = -1

while (found_at < s_len):
	found_at = s.find(word, found_at + 1, s_len)
	if (found_at == -1):
		break
	found += 1

print 'Number of times bob occurs is: ' + str(found)
