class PlayfairCipher:
    def __init__(self, key):
        self.key = key

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")
        key = key.upper()
        
        key_set = []
        for char in key:
            if char not in key_set:
                key_set.append(char)

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        remaining_letters = []
        for letter in alphabet:
            if letter not in key_set and letter != 'J':  # Loại bỏ 'J'
                remaining_letters.append(letter)
        
        matrix_flat = key_set + remaining_letters
        if len(matrix_flat) > 25:
            matrix_flat = matrix_flat[:25]
        elif len(matrix_flat) < 25:
            pass

        playfair_matrix = [matrix_flat[i:i+5] for i in range(0, len(matrix_flat), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1  # Không tìm thấy

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        processed_plain_text = ""
        i = 0
        while i < len(plain_text):
            if i + 1 < len(plain_text) and plain_text[i] == plain_text[i+1]:
                processed_plain_text += plain_text[i] + 'X'
                i += 1
            elif i + 1 == len(plain_text): 
                processed_plain_text += plain_text[i] + 'X'
                i += 1
            else:
                processed_plain_text += plain_text[i] + plain_text[i+1]
                i += 2

        encrypted_text = ""
        for i in range(0, len(processed_plain_text), 2):
            pair = processed_plain_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1 + 5) % 5]
                decrypted_text += matrix[row2][(col2 - 1 + 5) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1 + 5) % 5][col1]
                decrypted_text += matrix[(row2 - 1 + 5) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]
        
        # Loại bỏ 'X' nếu nó là ký tự padding
        decrypted_text = decrypted_text.replace('X', '')  # Loại bỏ các 'X' nếu là padding
        return decrypted_text

# Ví dụ sử dụng
key = "MONARCHY"
plain_text = "HELLO"

cipher = PlayfairCipher(key)
matrix = cipher.create_playfair_matrix(key)
encrypted_text = cipher.playfair_encrypt(plain_text, matrix)
decrypted_text = cipher.playfair_decrypt(encrypted_text, matrix)

print(f"Plaintext: {plain_text}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
