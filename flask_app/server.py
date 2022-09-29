from ast import Num
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def contador():
	if 'num' in session:
		session['num'] += 1
	else:
		session['num'] = 1

	return render_template("index.html")

@app.route('/contador2')
def aumentar():
	session['num'] += 1
	return redirect('/')

@app.route('/destroy_session')
def eliminar():
	session.clear()
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)