"""
Hay que instalar flask_sqlalchemy

$ pip install flask-sqlalchemy

"""
from flask import Flask, render_template, url_for, request, redirect

from flask_sqlalchemy import SQLAlchemy


app_db = Flask(__name__)
"""
Aqui a continuacion configuramos la base de datos, aqui seria la de MySQL si uso eso instead.
"""
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'


"""
Aqui a continuacion creamos un objeto SLQAlchemy dandole la app_db (nuestra Flask app) como alimento.
a ese objeto lo nombramos 'db', luego creamos una clase llamada "libros" y hereda de la clase 'Model'
que esta en el objeto 'db' (objeto SQLAlchemy), de forma que "libros" es nuestro modelo de la tabla "libros"
"""
db = SQLAlchemy(app_db)
class libros(db.Model):
"""
Aqui procedemos a agregar lo que serian los atributos de la clase, que son en si las coumnas (db.Column()) de la tabla "libros"
"""
  id = db.Column('libro_id', db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  author = db.Column(db.String(50))
  number_pgs = db.Column(db.Integer)
  
  def __init__(self, name, author, number_pgs):
    self.name = name
    self.author = author
    self.number_pgs = number_pgs
  
"""
Creamos la tabla usando esta funcion del objeto db:
db.create_all()
  
Usamos tambien las siguientes funciones de acuerdo a la accion:
  
Para insertar los registros primero
db.session.add(objeto del model (un objeto libro en esta app))
y luego
db.session.commit(()

Para eliminar los registros
db.session.delete(objeto del model (un objeto libro en esta app))
  
Para llamar todos los registros de libro (libros.qury.all() en nuestro ejemplo)
model.query.all() 
  
Pdemos igual usar filtros, por ejemplo
libros.query.filter_by(author = 'Elvis Poin').all()
"""
  
"""
Ahora a continuacion pasamos a disenar las views, primero la de home view que mostrara todos los libros
"""
  
@app_db.route('/')
def show_all():
  return render_template('show_all.html', libros = libros.query.all())

"""
Ahora procedemos a agregar la view para agregar los poderosos libros
esta view/ruta funcionara con dos metodos, get y post, y hara algo distinto dependiendo de cual metodo sea usado para generar
la request
"""

@app_db.route('/new', method=['GET', 'POST'])
def new():
  """
  Si el metodo es post, es decir un formulario es enviado como post
  """
  if request.method == 'POST':
    if not request.form['name'] or not request.form['author'] or not request.form['number_pgs']:
      """
      Usamos flash para generar un mensaje de error
      """
      flash('Por favor agregue todos los campos', 'error')
    else:
      libro = libros(request.form['name'],request.form['author'],request.form['number_pgs'])
      """
      libro es el objeto de tipo libros creado usando la clase libros 
      """
      db.session.add(libro)
      db.session.commit()
      flash('Libro creado')
      return redirect(url_for('show_all'))
  Return render_template('new.html')
      
  
