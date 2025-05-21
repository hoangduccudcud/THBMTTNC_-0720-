class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key = str(key)  # Đảm bảo key là chuỗi
        key_index = 0  # Khai báo key_index
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')  # Tính key_shift từ khóa
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1  # Tăng key_index sau mỗi ký tự đã mã hóa
            else:
                encrypted_text += char  # Nếu không phải chữ cái, giữ nguyên
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0  # Khai báo key_index
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')  # Tính key_shift từ khóa
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift + 26) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift + 26) % 26 + ord('a'))
                key_index += 1  # Tăng key_index sau mỗi ký tự đã giải mã
            else:
                decrypted_text += char  # Nếu không phải chữ cái, giữ nguyên
        return decrypted_text
