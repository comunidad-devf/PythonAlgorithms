"""Crack password using Caesar Algorithms."""

import caesar

cracks = 0

with open('users_database.csv', 'r') as users_database:
    lines = users_database.readlines()[1:]
    for line in lines:
        email = line.split(',')[0]
        encrypted_passwd = line.split(',')[1]
        encrypted_letter = ord(encrypted_passwd[0])
        plain_letter = ord(line.split(',')[2][0])
        key = int()
        passwd = str()
        if encrypted_letter > plain_letter:
            key = encrypted_letter - plain_letter
        else:
            key = 26 - (plain_letter - encrypted_letter)
        passwd = caesar.decrypt(encrypted_passwd, key).lower()
        cracks +=1
        print "Email:", email, "| Password:", passwd, "| Key:", key

print cracks, "passwords cracked successfully."
