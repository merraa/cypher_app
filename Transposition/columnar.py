def encrypt(text, key='3142'):
    columns = ['' for _ in range(len(key))]
    for i, char in enumerate(text):
        columns[i % len(key)] += char
    result = ''
    for num in sorted(zip(key, columns)):
        result += num[1]
    return result

def decrypt(cipher, key='3142'):
    col_lengths = [len(cipher) // len(key)] * len(key)
    for i in range(len(cipher) % len(key)):
        col_lengths[i] += 1

    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
    columns = {}
    i = 0
    for idx, _ in sorted_key:
        columns[idx] = cipher[i:i + col_lengths[idx]]
        i += col_lengths[idx]

    result = ''
    for i in range(len(cipher) // len(key) + 1):
        for j in range(len(key)):
            if i < len(columns[j]):
                result += columns[j][i]
    return result
