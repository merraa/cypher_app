from substitution import caesar, atbash, monoalphabetic
from transposition import rail_fence, columnar, route

def get_algorithms():
    print("\nChoose a Substitution Algorithm:")
    print("1. Caesar Cipher\n2. Atbash Cipher\n3. Monoalphabetic Cipher")
    sub_choice = input("Your choice: ")

    if sub_choice == "1":
        sub = caesar
    elif sub_choice == "2":
        sub = atbash
    else:
        sub = monoalphabetic

    print("\nChoose a Transposition Algorithm:")
    print("1. Rail Fence\n2. Columnar Transposition\n3. Route Cipher")
    trans_choice = input("Your choice: ")

    if trans_choice == "1":
        trans = rail_fence
    elif trans_choice == "2":
        trans = columnar
    else:
        trans = route

    return sub, trans
