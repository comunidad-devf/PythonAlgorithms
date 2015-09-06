"""Alternating Characters."""
text = raw_input("Give me a text: ")
last_letter = text[0]
deleted = 0
for i in range(1, len(text)):
    if last_letter == text[i]:
        deleted += 1
    last_letter = text[i]
print deleted
