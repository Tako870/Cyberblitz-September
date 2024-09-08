from flask import Flask, render_template, session, request, redirect, url_for
import os, json

def merge(src, dst) : 
    for key, value in src.items() : 
        if hasattr(dst, "__getitem__") :
            if dst.get(key) and type(value) == dict : 
                merge(value, dst.get(key))
            else : 
                dst[key] = value
        elif hasattr(dst, key) and type(value) == dict : 
            merge(value, getattr(dst,key))
        else : 
            setattr(dst, key, value)
			

class User : 
	def __init__(self, username) : 
		self.username = username
		pass
    

app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.urandom(32)) 
app.config['SESSION_COOKIE_HTTPONLY'] = False 
flag1 = '{...}'
first_access = True

thisUser = User('takotako')

@app.route('/')
@app.route('/index')
def index():
	global first_access
	if first_access :
		session['user'] = 'takotako'
		first_access = False
	properties = thisUser.__dict__
	return render_template('index.html', properties = properties)

@app.route("/<path:path>")
def render(path):
    if not os.path.exists(f"templates/{path}"):
        return render_template("message.html", code = 404, message = "not found")
    return render_template(f"{path}")

@app.route('/update_user')
def update_user() : 
	return render_template('update_user.html')

@app.route('/update', methods = ['POST'])
def update() : 
	user_json = json.loads(request.form['userJson'])
	merge(user_json, thisUser)
	return redirect(url_for('index'))

@app.route('/flag')
def flag() : 
	global flag1
	code = 'Unfortunate'
	message = 'No dice.'
	if session.get('user') == 'Ben Dover' :
		code = 'flag'
		message = flag1
	return render_template('message.html', code = code, message = message)

if __name__ == '__main__':
	app.run()