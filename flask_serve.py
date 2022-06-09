
from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def hello():
  return "Holix mundo"

app.run()
