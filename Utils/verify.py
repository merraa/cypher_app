def verify_output(original, decrypted):
    if original == decrypted:
        print("✅ Verification successful: Decryption matches original!")
    else:
        print("❌ Verification failed: Decryption does not match.")
