from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

if __name__ == '__main__':
    app.run(debug=True)
