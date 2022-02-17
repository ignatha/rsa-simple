from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
from itsdangerous import URLSafeSerializer
import rsa

app = Flask(__name__)
cors = CORS(app)
danger = URLSafeSerializer("296b8e8fde09d68f5ab4ef26d5295afc")

@app.route("/")
def index():
	return render_template('rsa/index.html')

@app.route("/generate",methods=['POST'])
def generate():
	p = request.form['p']
	q = request.form['q']

	rsa_s = rsa.rsa(int(p), int(q))
	rsa_s.setN()
	rsa_s.setM()
	rsa_s.setE()
	rsa_s.setD()

	public_key = danger.dumps(f'{rsa_s.n}.{rsa_s.e}')
	private_key = danger.dumps(f'{rsa_s.n}.{rsa_s.d}')

	data = dict([("public_key", public_key), ("private_key", private_key)])

	return jsonify(data)

@app.route("/enkripsi",methods=['POST'])
def enkripsi():
	public_key = request.form['public_key']
	public_key = danger.loads(public_key)
	public_key = public_key.split('.')

	text = request.form['plain_text']
	plainText = [int(ord(c)) for c in text]
	cipherText = [int(pow(s,int(public_key[1]),int(public_key[0]))) for s in plainText] 

	data = {
		"plain_text_ascii":plainText,
		"decrypt":cipherText
	}

	return jsonify(data)


@app.route("/decrypt",methods=['POST'])
def decrypt():
	private_key = request.form['private_key']
	private_key = danger.loads(private_key)
	private_key = private_key.split('.')

	text = request.form['cipher_text']
	ciphertext = text.split(' ')
	plain_text_ascii = [int(pow(int(s),int(private_key[1]),int(private_key[0]))) for s in ciphertext]
	plainText = [chr(c) for c in plain_text_ascii] 

	data = {
		"plain_text_ascii":plain_text_ascii,
		"plaintext":plainText
	}

	return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
