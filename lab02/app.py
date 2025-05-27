from flask import Flask, render_template, request
from ciphers.vigenere import VigenereCipher
from ciphers.railfence import RailFenceCipher
from ciphers.playfair import PlayfairCipher
from ciphers.transposition import TranspositionCipher
from ciphers.caesar import CaesarCipher

app = Flask(__name__)

# Route cho trang chính
@app.route('/')
def index():
    return render_template('index.html')

# Vigenère Cipher Routes
@app.route('/vigenere_encrypt', methods=['POST'])
def vigenere_encrypt():
    try:
        text = request.form['inputText']
        key = request.form['key']
        vigenere = VigenereCipher()
        encrypted_text = vigenere.encrypt_text(text, key)
        return render_template('vigenere.html', vigenere_encrypted_text=encrypted_text)
    except Exception as e:
        return render_template('vigenere.html', vigenere_encrypted_text=f"Error: {str(e)}")

@app.route('/vigenere_decrypt', methods=['POST'])
def vigenere_decrypt():
    try:
        text = request.form['inputText']
        key = request.form['key']
        vigenere = VigenereCipher()
        decrypted_text = vigenere.decrypt_text(text, key)
        return render_template('vigenere.html', vigenere_decrypted_text=decrypted_text)
    except Exception as e:
        return render_template('vigenere.html', vigenere_decrypted_text=f"Error: {str(e)}")

# Rail Fence Cipher Routes
@app.route('/railfence_encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        text = request.form['inputText']
        rails = int(request.form['rails'])
        if rails < 2:
            raise ValueError("Number of rails must be at least 2.")
        railfence = RailFenceCipher()
        encrypted_text = railfence.encrypt_text(text, rails)
        return render_template('railfence.html', railfence_encrypted_text=encrypted_text)
    except ValueError as e:
        return render_template('railfence.html', railfence_encrypted_text=f"Error: {str(e)}")
    except Exception as e:
        return render_template('railfence.html', railfence_encrypted_text=f"Error: {str(e)}")

@app.route('/railfence_decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        text = request.form['inputText']
        rails = int(request.form['rails'])
        if rails < 2:
            raise ValueError("Number of rails must be at least 2.")
        railfence = RailFenceCipher()
        decrypted_text = railfence.decrypt_text(text, rails)
        return render_template('railfence.html', railfence_decrypted_text=decrypted_text)
    except ValueError as e:
        return render_template('railfence.html', railfence_decrypted_text=f"Error: {str(e)}")
    except Exception as e:
        return render_template('railfence.html', railfence_decrypted_text=f"Error: {str(e)}")

# Playfair Cipher Routes
@app.route('/playfair_encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        text = request.form['inputText']
        key = request.form['key']
        if not text.isalpha() or not key.isalpha():
            raise ValueError("Text and key must contain only letters.")
        playfair = PlayfairCipher()
        encrypted_text = playfair.encrypt_text(text, key)
        return render_template('playfair.html', playfair_encrypted_text=encrypted_text)
    except Exception as e:
        return render_template('playfair.html', playfair_encrypted_text=f"Error: {str(e)}")

@app.route('/playfair_decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        text = request.form['inputText']
        key = request.form['key']
        if not text.isalpha() or not key.isalpha():
            raise ValueError("Text and key must contain only letters.")
        playfair = PlayfairCipher()
        decrypted_text = playfair.decrypt_text(text, key)
        return render_template('playfair.html', playfair_decrypted_text=decrypted_text)
    except Exception as e:
        return render_template('playfair.html', playfair_decrypted_text=f"Error: {str(e)}")

# Transposition Cipher Routes
@app.route('/transposition_encrypt', methods=['POST'])
def transposition_encrypt():
    try:
        text = request.form['inputText']
        key = int(request.form['key'])
        if key < 2:
            raise ValueError("Key must be at least 2.")
        transposition = TranspositionCipher()
        encrypted_text = transposition.encrypt_text(text, key)
        return render_template('transposition.html', transposition_encrypted_text=encrypted_text)
    except ValueError as e:
        return render_template('transposition.html', transposition_encrypted_text=f"Error: {str(e)}")
    except Exception as e:
        return render_template('transposition.html', transposition_encrypted_text=f"Error: {str(e)}")

@app.route('/transposition_decrypt', methods=['POST'])
def transposition_decrypt():
    try:
        text = request.form['inputText']
        key = int(request.form['key'])
        if key < 2:
            raise ValueError("Key must be at least 2.")
        transposition = TranspositionCipher()
        decrypted_text = transposition.decrypt_text(text, key)
        return render_template('transposition.html', transposition_decrypted_text=decrypted_text)
    except ValueError as e:
        return render_template('transposition.html', transposition_decrypted_text=f"Error: {str(e)}")
    except Exception as e:
        return render_template('transposition.html', transposition_decrypted_text=f"Error: {str(e)}")

# Caesar Cipher Routes
@app.route('/caesar_encrypt', methods=['POST'])
def caesar_encrypt():
    try:
        text = request.form['inputText']
        key = int(request.form['key'])
        caesar = CaesarCipher()
        encrypted_text = caesar.encrypt_text(text, key)
        return render_template('caesar.html', caesar_encrypted_text=encrypted_text)
    except ValueError as e:
        return render_template('caesar.html', caesar_encrypted_text=f"Error: {str(e)}")
    except Exception as e:
        return render_template('caesar.html', caesar_encrypted_text=f"Error: {str(e)}")

@app.route('/caesar_decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        text = request.form['inputText']
        key = int(request.form['key'])
        caesar = CaesarCipher()
        decrypted_text = caesar.decrypt_text(text, key)
        return render_template('caesar.html', caesar_decrypted_text=decrypted_text)
    except ValueError as e:
        return render_template('caesar.html', caesar_decrypted_text=f"Error: {str(e)}")
    except Exception as e:
        return render_template('caesar.html', caesar_decrypted_text=f"Error: {str(e)}")

# Route cho các trang HTML riêng lẻ
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/transposition')
def transposition():
    return render_template('transposition.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)