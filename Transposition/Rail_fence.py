def encrypt(text, rails=3):
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction = 1
    for i, char in enumerate(text):
        fence[rail][i] = char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join(''.join(row) for row in fence)

def decrypt(cipher, rails=3):
    fence = [['' for _ in range(len(cipher))] for _ in range(rails)]
    rail = 0
    direction = 1
    marker = [['' for _ in range(len(cipher))] for _ in range(rails)]
    
    for i in range(len(cipher)):
        marker[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if marker[r][c] == '*' and index < len(cipher):
                fence[r][c] = cipher[index]
                index += 1

    result = ''
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        result += fence[rail][i]
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return result
