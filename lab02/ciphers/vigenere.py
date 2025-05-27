class VigenereCipher:
    def encrypt_text(self, text, key):
        text = text.upper()
        key = key.upper()
        encrypted = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - 65
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
                key_index += 1
            else:
                encrypted += char
        return encrypted

    def decrypt_text(self, text, key):
        text = text.upper()
        key = key.upper()
        decrypted = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - 65
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
                key_index += 1
            else:
                decrypted += char
        return decrypted