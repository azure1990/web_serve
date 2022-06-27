from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#importing rutes
from rutas import *
from modelos import *

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.secret_key = "0256ac1229d70c6056e9ca7d40a014ae4ff730cac62ba81f"



"""
@d_app.route('/thankyou.html')
def love():
  return render_template('thankyou.html')
@d_app('/about.html')
def about():
  return render_template('about.html')
@d_app('/works.html')
def work():
  return render_template('works.html')
@d_app('/contact.html')
def contact():
  return render_template('works.html')
@d_app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name)
def write_to_file(data):
  with open("database.txt", mode='a') as database:
    email = data['email']
    subject = data['subject']
    message = data['message']
    file = database.write(f"{email},{subject},{message}"")
def write_to_file(data):
  with open("database.txt", mode='a') as database:
    file = database.write(f'{data}')
@d_app.route('/submit_form', methods = ['POST', 'GET'])
def submit_f():
  if request.method=='POST':
    data = request.form.to_dict()
    write_to_file(data)
    return redirect('/thankyou.html')
  else:
    return "Something went wrong"
"""