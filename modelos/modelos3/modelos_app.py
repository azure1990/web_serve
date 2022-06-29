from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#importing rutes

#from rutas import *
#from modelos import *

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///losmodelos3.sqlite3'
app.secret_key = "0256ac1229d70c6056e9ca7d40a014ae4ff730cac62ba81f"
db = SQLAlchemy(app)

class Comensal(db.Model):

	id = db.Column('id', db.Integer, primary_key = True)
	nombre = db.Column(db.String(100))
	comedores = 

	def __init__(self, nombre):
		self.nombre = nombre

class Comedor(db.Model):
  
  	id = db.Column('id', db.Integer, primary_key = True, unique = True)
  	nombre = db.Column(db.String(100))
  	comensales =

  	def __init__(self, nombre):

  		self.nombre = nombre  		
	


@app.route('/')
def mostrar_comedores():
  	return render_template('comedores.html', amos = Comedor.query.all())

@app.route('/')
def mostrar_comensales():
  	return render_template('comensales.html', amos = Comensal.query.all())


@app.route('/nuevo_comedor', methods=['GET', 'POST'])
def nuevo_comedor():
	if request.method == 'POST':
		if not request.form['nombre']:
			flash('Por favor agrega el nombre del nuevo comedors', 'error')
		else:
			comedor = Comedor(request.form['nombre'])
			db.session.add(comedor)
			db.session.commit()
			flash('Comedor creado')
			return redirect('/')  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('crear_comedor.html')

@app.route('/nuevo_comedor', methods=['GET', 'POST'])
def nuevo_comensal():
	if request.method == 'POST':
		if not request.form['nombre']:
			flash('Por favor agrega el nombre del nuevo comensal', 'error')
		else:
			comensal = Comensal(request.form['nombre'])
			db.session.add(comedor)
			db.session.commit()
			flash('Comensal creado')
			return redirect('/')  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('crear_comensal.html')

