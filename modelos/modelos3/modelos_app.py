from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#importing rutes

#from rutas import *
#from modelos import *

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///losmodelos3.sqlite3'
app.secret_key = "0256ac1229d70c6056e9ca7d40a014ae4ff730cac62ba81f"
db = SQLAlchemy(app)


tags = db.Table('clientex',
    db.Column('comensal_id', db.Integer, db.ForeignKey('comensal.id'), primary_key=True),
    db.Column('comedor_id', db.Integer, db.ForeignKey('comedor.id'), primary_key=True)
)


class Comensal(db.Model):

	id = db.Column('id', db.Integer, primary_key = True)
	nombre = db.Column(db.String(100))
	comedores = db.relationship('Comedor', secondary=clientex, lazy=True, backref=db.backref('comensales', lazy=True))
	#otra forma es: comedores = db.relationship('Comedor', secondary=clientex, lazy=True, 'comensales')
	def __init__(self, nombre):
		self.nombre = nombre

class Comedor(db.Model):
  
  	id = db.Column('id', db.Integer, primary_key = True, unique = True)
  	nombre = db.Column(db.String(100))
  	#comensales = db.relationship('Comensal', secondary=clientex, lazy='subquery',
        #backref=db.backref('comedores', lazy=True))

  	def __init__(self, nombre):
		
  		self.nombre = nombre  		

		
		
#db.create_all()

@app.route('/')
def mostrar_comedores():
  	return render_template('comedores.html', comedores = Comedor.query.all())

@app.route('/comensales')
def mostrar_comensales():
  	return render_template('comensales.html', comensales = Comensal.query.all())


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

@app.route('/nuevo_comensal', methods=['GET', 'POST'])
def nuevo_comensal():
	if request.method == 'POST':
		if not request.form['nombre']:
			flash('Por favor agrega el nombre del nuevo comensal', 'error')
		else:
			comensal = Comensal(request.form['nombre'])
			db.session.add(comedor)
			db.session.commit()
			flash('Comensal creado')
			return redirect('/comensales')  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('crear_comensal.html')

@app.route('/clientes/<int:comedorid>')
def clientes(comedorid):
	return render_template('clientes.html', comensales = Comedor.query.filter_by(id = comedorid).comensales)
			       

@app.route('/favoritos/<int:comemsalid>')
def favoritos(comensalid):
	return render_template('favoritos.html', comedores = Comensal.query.filter_by(id = comensalid).comedores)


@app.route('/agregar_cliente/<int:comedor_id>')
def agregar_cliente(comedor_id):
	if request.method == 'POST':
		if not request.form['client']:
			flash('Por favor elija un cliente', 'error')
		else:
			comedor = Comedor.query.filter_by(id = comedor_id).first())
			comensal = Comensal.query.filter_by(id = form['cliente']).first())
			comedor.comensales.append(comensal)
			db.session.commit(comedor)
			flash('Cliente agregado')
			return redirect(url_for('clientes', comedorid = comedor_id))  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('agregar_cliente.html',  comensales = Comensal.query.all())


@app.route('/agregar_favorito/<int:comensal_id>')
def agregar_favorito(comensal_id):
	if request.method == 'POST':
		if not request.form['prefereti']:
			flash('Por favor elija un comedor', 'error')
		else:
			comensal = Comensal.query.filter_by(id = comensal_id).first())
			comedor = Comedor.query.filter_by(id = form['prefereti']).first())
			comensal.comensales.append(comedor)
			db.session.commit(comensal)
			flash('Favorito agregado')
			return redirect(url_for('favoritos', comensalid = comensal_id))  
			#print(request.form['nombre'])
			#return request.form['nombre']
	return render_template('agregar_favorito.html', comedores = Comedor.query.all())
