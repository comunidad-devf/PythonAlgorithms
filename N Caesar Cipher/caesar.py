"""Caesar Cipher."""


def encrypt(plain_text, key):
    """Encrypt plain text."""
    cipher_text = ''
    for letter in plain_text.upper():
        if letter == ' ':
            cipher_text += letter
        elif ord(letter) > 90 - key:
            cipher_text += chr(ord(letter) - (26 - key))
        else:
            cipher_text += chr(ord(letter) + key)
    return cipher_text


def decrypt(cipher_text, key):
    """Decrypt cipher text."""
    plain_text = ''
    for letter in cipher_text.upper():
        if letter == ' ':
            plain_text += letter
        elif ord(letter) < 65 + key:
            plain_text += chr(ord(letter) + (26 - key))
        else:
            plain_text += chr(ord(letter) - key)
    return plain_text

method = raw_input("Type [e/E] for encrypt or [d/D] for decrypt: ")

text = raw_input("Enter a text (Only letters): ")
key = int(raw_input("Enter the key [1..25]: "))
if method in ['e', 'E']:
    text = encrypt(text, key)
    print "Cipher text:", text
else:
    text = decrypt(text, key)
    print "Plain text:", text
