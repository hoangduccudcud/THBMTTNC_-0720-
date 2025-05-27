class TranspositionCipher:
    def encrypt_text(self, text, key):
        key = int(key)
        n = len(text)
        if n % key != 0:
            text += " " * (key - n % key)  # Padding với khoảng trắng
        col = len(text) // key
        matrix = [list(text[i:i + col]) for i in range(0, len(text), col)]
        encrypted = ""
        for j in range(col):
            for i in range(key):
                encrypted += matrix[i][j]
        return encrypted

    def decrypt_text(self, text, key):
        key = int(key)
        col = len(text) // key
        matrix = [['' for _ in range(col)] for _ in range(key)]
        index = 0
        for j in range(col):
            for i in range(key):
                matrix[i][j] = text[index]
                index += 1
        decrypted = ""
        for i in range(key):
            for j in range(col):
                decrypted += matrix[i][j]
        return decrypted.strip()