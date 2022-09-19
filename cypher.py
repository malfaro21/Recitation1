# Division of PEMaCS
# CSCI-121 Elements of Computer Programming II
# Recitation 1 - Encryption with a password
# *******************************************************

import math
import string
alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}

def encrypt(message, password):
    encrypted_message = ''

    for index, ch in enumerate(message):
        pass_ch = password[index % len(password)]
        key = ordinal_value[pass_ch]
        ord_of_character = ordinal_value[ch]
        shifted_ord_of_characters = (ord_of_character + key) % len(alphabet)
        encrypted_characters = alphabet[shifted_ord_of_characters]
        encrypted_message += encrypted_characters
    return encrypted_message


def decrypt(message, password):
    encrypted_message = ''

    for index, ch in enumerate(message):
        pass_ch = password[index % len(password)]
        key = ordinal_value[pass_ch]
        ord_of_character = ordinal_value[ch]
        shifted_ord_of_characters = (ord_of_character - key) % len(alphabet)
        encrypted_characters = alphabet[shifted_ord_of_characters]
        encrypted_message += encrypted_characters

    return encrypted_message
