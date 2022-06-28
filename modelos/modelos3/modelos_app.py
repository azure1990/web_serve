from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#importing rutes

#from rutas import *
#from modelos import *

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///losmodelos.sqlite3'
app.secret_key = "0256ac1229d70c6056e9ca7d40a014ae4ff730cac62ba81f"
db = SQLAlchemy(app)

class Amo(db.Model):

	id = db.Column('id', db.Integer, primary_key = True)
	nombre = db.Column(db.String(100))
	perros = db.relationship('Perro', backref='amo', lazy=True)


	def __init__(self, nombre):
		self.nombre = nombre

class Perro(db.Model):
  
  	id = db.Column('id', db.Integer, primary_key = True, unique = True)
  	nombre = db.Column(db.String(100))
  	edad = db.Column(db.Integer)
  	amo_id = db.Column(db.Integer, db.ForeignKey('amo.id'), nullable=False)

  	def __init__(self, nombre, edad, amo_id):

  		self.nombre = nombre
  		self.edad = edad
  		self.amo_id=amo_id
	


@app.route('/')
def mostrar_amos():
  	return render_template('amos.html', amos = Amo.query.all())


@app.route('/nuevo_amo', methods=['GET', 'POST'])
def nuevo_amo():
	if request.method == 'POST':
		if not request.form['nombre']:
			flash('Por favor agrega el nombre del nuevo amo', 'error')
		else:
			amo = Amo(request.form['nombre'])
			db.session.add(amo)
			db.session.commit()
			flash('Amo creado')
			return redirect('/')  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('crear_amo.html')



@app.route('/perro/<int:amo_id>', methods=['GET', 'POST'])
def crear_perro(amo_id):
	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['edad']:
			flash('Por favor llena todo los campos', 'error')
		else:
			perro = Perro(request.form['nombre'],request.form['edad'], amo_id)
			db.session.add(perro)
			db.session.commit()
			flash('perro creado')
			return redirect('/')  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('nuevo_perro.html', amo = amo_id)

@app.route('/perros/<int:amo>')
def perros(amo):
	return render_template('perros.html', perros = Perro.query.filter_by(amo_id = amo).all())
