import itertools

def decrypt_monoalphabetic_brute_force(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()
    
    for perm in itertools.permutations(alphabet):
        key_map = dict(zip(perm, alphabet))
        decrypted_text = "".join(key_map.get(c, c) for c in ciphertext)
        print(decrypted_text)

if __name__ == "__main__":
    encrypted_text = input("Enter encrypted message: ")
    print("Brute Force Attack Results:")
    decrypt_monoalphabetic_brute_force(encrypted_text)