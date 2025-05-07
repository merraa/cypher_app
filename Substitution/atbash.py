def encrypt(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(155 - ord(char))  # 65 + 90 = 155
        elif char.islower():
            result += chr(219 - ord(char))  # 97 + 122 = 219
        else:
            result += char
    return result

def decrypt(text):
    return encrypt(text)  # Atbash is symmetric
