import math

def encrypt(text, cols=4):
    rows = math.ceil(len(text) / cols)
    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(text):
                matrix[r][c] = text[idx]
                idx += 1
    return ''.join(''.join(row) for row in zip(*matrix))  # column-wise read

def decrypt(cipher, cols=4):
    rows = math.ceil(len(cipher) / cols)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for c in range(cols):
        for r in range(rows):
            if idx < len(cipher):
                matrix[r][c] = cipher[idx]
                idx += 1
    return ''.join(''.join(row) for row in matrix)
