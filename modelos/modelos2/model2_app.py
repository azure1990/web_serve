from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#importing rutes

#from rutas import *
#from modelos import *

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///losmodelos2.sqlite3'
app.secret_key = "0256ac1229d70c6056e9ca7d40a014ae4ff730cac62ba81f"
db = SQLAlchemy(app)

class Libro(db.Model):

	id = db.Column('id', db.Integer, primary_key = True)
	nombre = db.Column(db.String(100))
	autor_id = db.relationship('Autor', backref='libro', lazy=True)

	def __init__(self, nombre, autor_id):


		self.nombre = nombre
		self.autor_id = autor_id

class Autor(db.Model):
  
  	id = db.Column('id', db.Integer, primary_key = True, unique = True)
  	nombre = db.Column(db.String(100))
  	libro_id = db.relationship('Libro', backref='autor', lazy=True)

  	def __init__(self, nombre, libro_id):

  		self.nombre = nombre
  		self.libro_id = libro_id
	
#db.create_all()

@app.route('/')
def mostrar_libros():
  	return render_template('libros.html', libros = Libro.query.all())

 @app.route('/')
def mostrar_autores():
  	return render_template('autores.html', libros = Libro.query.all()) 	


@app.route('/nuevo_libro', methods=['GET', 'POST'])
def nuevo_libro():
	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['autor_id']:
			flash('Por favor rellene todos los campos', 'error')
		else:
			libro = Libro(request.form['nombre'], request.form['autor_id'])
			db.session.add(libro)
			db.session.commit()
			flash('Libro creado')
			return redirect('/')  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('nuevo_libro.html')


@app.route('/nuevo_autor', methods=['GET', 'POST'])
def nuevo_autor():
	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['libro_id']:
			flash('Por favor rellene todos los campos', 'error')
		else:
			libro = Libro(request.form['nombre'], request.form['libro_id'])
			db.session.add(libro)
			db.session.commit()
			flash('Autor creado')
			return redirect('/')  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('nuevo_autor.html')




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