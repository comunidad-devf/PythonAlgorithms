"""Take the longer alphabetical substring."""

text = raw_input("Give me a text plz: ")
max_len = 0
substring_id = 0
max_subsitring_id = 0

text_len = len(text)

while substring_id < text_len:
    if (text_len - substring_id <= max_len):
        break
    cur_len = 1
    
    start_idx = substring_id
    while (substring_id + 1 < text_len and text[substring_id] <= text[substring_id + 1]):
        cur_len += 1
        substring_id += 1
        
    if (cur_len > max_len):
        max_len = cur_len
        max_subsitring_id = start_idx
        
    substring_id += 1

winner = text[max_subsitring_id:max_subsitring_id+max_len]
print 'The longest alphabetical string in', text, 'is', str(winner)