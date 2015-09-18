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
