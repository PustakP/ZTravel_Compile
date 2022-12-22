from flask import Flask, render_template, send_file, redirect, request, send_from_directory
from threading import Thread
import db 


app = Flask('ZTravel')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/portal')
def portal():
   return render_template('portal.html')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == "POST":
       email = request.form.get("email")
       password = request.form.get("password")
       name = request.form.get("name")
       db.register_user(name, email, password)
    return render_template('signup.html')

@app.route('/confirm')
def confirm():
   return render_template('confirm.html')

@app.route('/flights')
def flights():
   return render_template('flights.html')

@app.route('/logout')
def logout():
   return render_template('logout.html')

@app.route('/profile')
def profile():
   return render_template('profile.html')

@app.route('/commercial')
def commercial():
   return render_template('commercial.html')

@app.route('/tours')
def tours():
   return render_template('tours.html')

@app.route('/warn')
def warn():
   return render_template('warn.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
  if request.method == "POST":
       email = request.form.get("email")
       password = request.form.get("password")
       db.login(email, password)
  return render_template('login.html')

def start_server():
  app.run(host='0.0.0.0',port=8080)
  
t = Thread(target=start_server)
t.start()