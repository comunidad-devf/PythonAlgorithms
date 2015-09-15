import string

class Caesar():

    plain_text = ""
    cipher_text = []
    valid_text = True

    def encrypt(self, plain_text, ROT=None):
        plain_text = plain_text.upper()
        self.plain_text = plain_text
        for letter in plain_text:
            if letter not in string.uppercase + ' \n':
                self.valid_text = False
                break
        if not self.valid_text:
            return None
        else:
            if ROT:
                cipher_text = ""
                for letter in plain_text:
                    if letter == ' ' or letter == '\n':
                        cipher_text += letter
                    elif ord(letter) > (90 - ROT):
                        cipher_text += chr(ord(letter) - (26 - ROT))
                    else:
                        cipher_text += chr(ord(letter) + ROT)
                self.cipher_text = cipher_text
                return self.cipher_text
            else:
                rots = []
                for i in range(1, 26):
                    cipher_text = ""
                    for letter in plain_text:
                        if letter == ' ' or letter == '\n':
                            cipher_text += letter
                        elif ord(letter) > (90 - i):
                            cipher_text += chr(ord(letter) - (26 - i))
                        else:
                            cipher_text += chr(ord(letter) + i)
                    rot_name = 'ROT ' + str(i)
                    actual_rot = {
                        'ROT': rot_name,
                        'cipherText': cipher_text,
                    }
                    rots.append(actual_rot)
                self.cipher_text = rots
                return self.cipher_text

    def decrypt(self, cipher_text):
        pass
