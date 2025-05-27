class PlayfairCipher:
    def create_matrix(self, key):
        key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Loại bỏ trùng lặp và thay J bằng I
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Bỏ J
        key += "".join(char for char in alphabet if char not in key)
        matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
        return matrix

    def find_position(self, char, matrix):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None

    def encrypt_text(self, text, key):
        text = text.upper().replace("J", "I")
        text = "".join(char for char in text if char.isalpha())
        if len(text) % 2 == 1:
            text += "X"
        pairs = [text[i:i+2] for i in range(0, len(text), 2)]
        matrix = self.create_matrix(key)
        encrypted = ""

        for a, b in pairs:
            row1, col1 = self.find_position(a, matrix)
            row2, col2 = self.find_position(b, matrix)
            if row1 == row2:
                encrypted += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted += matrix[row1][col2] + matrix[row2][col1]
        return encrypted

    def decrypt_text(self, text, key):
        text = text.upper()
        pairs = [text[i:i+2] for i in range(0, len(text), 2)]
        matrix = self.create_matrix(key)
        decrypted = ""

        for a, b in pairs:
            row1, col1 = self.find_position(a, matrix)
            row2, col2 = self.find_position(b, matrix)
            if row1 == row2:
                decrypted += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted += matrix[row1][col2] + matrix[row2][col1]
        return decrypted