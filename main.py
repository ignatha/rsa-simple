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

	rsa_bowo = rsa.rsa(int(p), int(q))
	rsa_bowo.setN()
	rsa_bowo.setM()
	rsa_bowo.setE()
	rsa_bowo.setD()

	data = dict([('n', rsa_bowo.n), ('m', rsa_bowo.m), ('e', rsa_bowo.e), ('d', rsa_bowo.d)])

	return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')