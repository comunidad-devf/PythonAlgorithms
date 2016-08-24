"""Caesar Cipher."""

from string import ascii_uppercase as POOL
from string import ascii_lowercase as pool


def caesar(plain_text, key):
    cipher_text = ''

    for char in plain_text:
        if not char.isalpha():
            cipher_text += char
        else:
            if char.isupper():
                cipher_text += POOL[(POOL.find(char) + key) % 26]
            else:
                cipher_text += pool[(pool.find(char) + key) % 26]
    return cipher_text


def encrypt(plain_text, key):
    return caesar(plain_text, key)


def decrypt(cipher_text, key):
    return caesar(cipher_text, -key)

method = raw_input("Type [e/E] for encrypt or [d/D] for decrypt: ")

text = raw_input("Enter a text: ")
key = int(raw_input("Enter the key [1..25]: "))
if method in ['e', 'E']:
    text = encrypt(text, key)
    print "Cipher text:", text
else:
    text = decrypt(text, key)
    print "Plain text:", text
