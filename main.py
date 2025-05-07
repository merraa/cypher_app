from menu import get_algorithms
from utils.verify import verify_output

def main():
    print("\n==== Cipher Application ====")
    plaintext = input("Enter the plaintext: ")

    sub_algo, trans_algo = get_algorithms()

    encrypted_sub = sub_algo.encrypt(plaintext)
    encrypted = trans_algo.encrypt(encrypted_sub)

    print(f"\nEncrypted Text: {encrypted}")

    decrypted_trans = trans_algo.decrypt(encrypted)
    decrypted = sub_algo.decrypt(decrypted_trans)

    print(f"Decrypted Text: {decrypted}")
    verify_output(plaintext, decrypted)

if __name__ == "__main__":
    main()
