from collections import Counter

def frequency_analysis_decrypt(ciphertext):
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    ciphertext = ciphertext.upper()
    letter_counts = Counter(filter(str.isalpha, ciphertext))
    sorted_letters = [letter for letter, _ in letter_counts.most_common()]
    
    key_map = dict(zip(sorted_letters, english_freq))
    
    decrypted_text = "".join(key_map.get(c, c) for c in ciphertext)
    
    return decrypted_text

if __name__ == "__main__":
    encrypted_text = input("Enter the encrypted text: ")
    decrypted_text = frequency_analysis_decrypt(encrypted_text)
    print("\nMost Likely Decryption:")
    print(decrypted_text)
