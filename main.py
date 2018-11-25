from flask import Flask, request, jsonify, render_template, url_for
import rsa

app = Flask(__name__)

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

	data = dict([('n', rsa_s.n), ('m', rsa_s.m), ('e', rsa_s.e), ('d', rsa_s.d)])

	return jsonify(data)

@app.route("/enkripsi",methods=['POST'])
def enkripsi():
	e = request.form['public_key']
	n = request.form['nilai_n']
	text = request.form['plain_text']
	plainText = [int(ord(c)) for c in text]
	cipherText = [int(pow(s,int(e),int(n))) for s in plainText] 

	data = {
		"plain_text_ascii":plainText,
		"decrypt":cipherText
	}

	return jsonify(data)


@app.route("/decrypt",methods=['POST'])
def decrypt():
	d = request.form['private_key']
	n = request.form['nilai_n_decrypt']
	text = request.form['cipher_text']
	ciphertext = text.split(' ')
	plain_text_ascii = [int(pow(int(s),int(d),int(n))) for s in ciphertext]
	plainText = [chr(c) for c in plain_text_ascii] 

	data = {
		"plain_text_ascii":plain_text_ascii,
		"plaintext":plainText
	}

	return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')