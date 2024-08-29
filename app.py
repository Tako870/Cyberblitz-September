from flask import Flask, render_template, session, request, redirect, url_for
import os, json

app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.urandom(32)) 
app.config['SESSION_COOKIE_HTTPONLY'] = False 
flag = '{...}'
first_access = True

@app.route('/')
@app.route('/index')
def index():
	global first_access
	if first_access :
		session['user'] = 'takotako'
		first_access = False
	return render_template('index.html')

@app.route('/update_user')
def update_user() : 
	return render_template('update_user.html')

@app.route('/update', methods = ['POST'])
def update() : 
	user_json = request.form['userJson']
	print(json.loads(user_json))
	return redirect(url_for('index'))

@app.route('/flag')
def flag() : 
	code = 'Unfortunate'
	message = 'No dice.'
	if session.get('user') == 'Ben Dover' :
		code = 'flag'
		message = flag
	return render_template('message.html', code = code, message = message)

if __name__ == '__main__':
	app.run()