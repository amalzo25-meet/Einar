from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import random
import pyrebase

app = Flask(__name__, 
	template_folder = 'templates',
	static_folder = 'static')
app.config['SECRET_KEY'] = '*******'

	firebaseConfig = {
  "apiKey": "AIzaSyA6NzEKqu0zoIxiD9p_cP5QY9qCaobl3rE",
  "authDomain": "einarsite.firebaseapp.com",
  "projectId": "einarsite",
  "storageBucket": "einarsite.appspot.com",
  "messagingSenderId": "533850582861",
  "appI": "1:533850582861:web:50e9eed111a66468b95104",
  "measurementId" : "G-KCCV4G4SYH"
  "databaseURL": "https://einarsite-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
@app.route('/')
def about():
	return render_template("about.html")

@app.route('/signup', methods = ['POST', 'GET'])
def signup():

	if request.method == 'GET':
		return render_template("signup.html")

	else:

		email = request.form['email']
		password = request.form['password']
		fullname = request.form['fullname']
		username = request.form['username']
		
		try:

			login_session['users'] = auth.create_user_with_email_and_password(email, password)
			user_id = login_session['users']['localId']


			return redirect('home')

		except Exception as a:

			print(a)
			error = "failed"
			return render_template("signup.html")

@app.route('/signin', methods = ['POST', 'GET'])
def signin():
	if request.method == 'GET':
		return render_template("signin.html")
	else:
		email = request.form['email']
		password = request.form['password']

		try:

			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('home'))
		
		except:
			error = "failed"
			print(error)
			return render_template("signin.html")



if __name__ == "__main__":
	app.run(debug=True)