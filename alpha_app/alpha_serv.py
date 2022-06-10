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
def hello_index():
  return render_template("index.html")

@alpha_app.route('/templates/index.html')
def hello_html():
  return render_template("index.html")

@alpha_app.route('/templates/about.html')
def about():
  return render_template("about.html")


@alpha_app.route('/templates/services.html')
def serv():
  return render_template("services.html")


@alpha_app.route('/templates/contact.html')
def cont():
  return render_template("contact.html")


@alpha_app.route('/templates/components.html')
def comp():
  return render_template("components.html")



alpha_app.run()
