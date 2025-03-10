def generate_playfair_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    matrix = []
    
    for char in keyword:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def playfair_encrypt_decrypt(text, matrix, encrypt=True):
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text)) 
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            b = "X"
            i -= 1
        pairs.append((a, b))
        i += 2

    result = ""
    for a, b in pairs:
        pos1 = find_position(matrix, a)
        pos2 = find_position(matrix, b)

        if pos1 is None or pos2 is None:
            print(f"Error: Character '{a}' or '{b}' not found in matrix.")
            return ""

        row1, col1 = pos1
        row2, col2 = pos2

        if row1 == row2:
            result += matrix[row1][(col1 + (1 if encrypt else -1)) % 5]
            result += matrix[row2][(col2 + (1 if encrypt else -1)) % 5]
        elif col1 == col2:
            result += matrix[(row1 + (1 if encrypt else -1)) % 5][col1]
            result += matrix[(row2 + (1 if encrypt else -1)) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


if __name__ == "__main__":
    keyword = input("Enter keyword: ")
    matrix = generate_playfair_matrix(keyword)
    
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    
    choice = input("Encrypt or Decrypt (E/D): ").strip().upper()
    text = input("Enter text: ")
    
    if choice == "E":
        result = playfair_encrypt_decrypt(text, matrix, encrypt=True)
        print("Encrypted Text:", result)
    elif choice == "D":
        result = playfair_encrypt_decrypt(text, matrix, encrypt=False)
        print("Decrypted Text:", result)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
