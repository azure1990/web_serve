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
  
  Para insertar los registros
  db.session.add(objeto del model (un objeto libro en esta app))
  
  Para eliminar los registros
  db.session.delete(objeto del model (un objeto libro en esta app))
  
  Para llamar todos los registros de libro (libros.qury.all() en nuestro ejemplo)
  model.query.all() 
  
  Pdemos igual usar filtros, por ejemplo
  libros.query.filter_by(author = 'Elvis Poin').all()
  """
  
  """
  Ahora a continuacion pasamos a disenar las views
  """
  
  @app_db.route('/')
  def show_all():
    return render_template('show_all.html', libros = libros.query.all())
