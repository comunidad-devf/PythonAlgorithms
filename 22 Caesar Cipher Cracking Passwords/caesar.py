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
