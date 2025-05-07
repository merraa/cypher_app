import random
import string

key = dict(zip(string.ascii_lowercase, random.sample(string.ascii_lowercase, 26)))
reverse_key = {v: k for k, v in key.items()}

def encrypt(text):
    result = ""
    for char in text:
        if char.islower():
            result += key[char]
        elif char.isupper():
            result += key[char.lower()].upper()
        else:
            result += char
    return result

def decrypt(text):
    result = ""
    for char in text:
        if char.islower():
            result += reverse_key[char]
        elif char.isupper():
            result += reverse_key[char.lower()].upper()
        else:
            result += char
    return result
