from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok

alpha_app = Flask(__name__)
run_with_ngrok(alpha_app)

@alpha_app.route('/')
def hello():
  return render_template("index.html")

@alpha_app.route('/index')
def hello():
  return render_template("index.html")

@alpha_app.route('/index.html')
def hello():
  return render_template("index.html")



alpha_app.run()
