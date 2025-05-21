from flask import Flask, request, jsonify  # type: ignore
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher  # Thêm vào phần đầu của file api.py

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = int(data.get('key', 0))  # Sử dụng get để tránh lỗi nếu key không có
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = int(data.get('key', 0))  # Sử dụng get để tránh lỗi nếu key không có
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# RAILFENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = int(data.get('key', 0))  # Sử dụng get để tránh lỗi nếu key không có
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = int(data.get('key', 0))  # Sử dụng get để tránh lỗi nếu key không có
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data.get('key')
    playfair_cipher = PlayfairCipher(key)  # Khởi tạo với khóa người dùng cung cấp
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')
    playfair_cipher = PlayfairCipher(key)  # Khởi tạo với khóa người dùng cung cấp
    matrix = playfair_cipher.create_playfair_matrix(key)  # Cập nhật ma trận với khóa mới
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    playfair_cipher = PlayfairCipher(key)  # Khởi tạo với khóa người dùng cung cấp
    matrix = playfair_cipher.create_playfair_matrix(key)  # Tạo ma trận Playfair từ khóa
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)  # Truyền ma trận vào
    return jsonify({'decrypted_text': decrypted_text})

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# TRANSPOSITION CIPHER ALGORITHM
transposition_cipher = TranspositionCipher()  # Tạo một thể hiện của lớp TranspositionCipher

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()  # Lấy dữ liệu JSON từ request
    plain_text = data.get('plain_text')  # Trích xuất 'plain_text'
    key = int(data.get('key'))  # Trích xuất 'key' và chuyển đổi sang số nguyên
    encrypted_text = transposition_cipher.encrypt(plain_text, key)  # Gọi hàm mã hóa
    return jsonify({'encrypted_text': encrypted_text})  # Trả về kết quả mã hóa dưới dạng JSON

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()  # Lấy dữ liệu JSON từ request
    cipher_text = data.get('cipher_text')  # Trích xuất 'cipher_text'
    key = int(data.get('key'))  # Trích xuất 'key' và chuyển đổi sang số nguyên
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)  # Gọi hàm giải mã
    return jsonify({'decrypted_text': decrypted_text})  # Trả về kết quả giải mã dưới dạng JSON

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
