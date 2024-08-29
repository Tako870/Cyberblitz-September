from flask import Flask, render_template, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.urandom(32)) 
app.config['SESSION_COOKIE_HTTPONLY'] = False 
flag = '{...}'

@app.route('/')
@app.route('/index')
def index():
	session['user'] = 'takotako'
	return render_template('index.html')

@app.route('/flag')
def flag() : 
	message = 'No dice.'
	if session.get('user') == 'Ben Dover' :
		message = flag
	return render_template('flag.html', message = message)

if __name__ == '__main__':
	app.run()