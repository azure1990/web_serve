from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date
#importing rutes
#from rutas import *
#from modelos import *

d_app = Flask(__name__)

d_app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
d_app.secret_key = "0256ac1229d70c6056e9ca7d40a014ae4ff730cac62ba81f"

db = SQLAlchemy(d_app)

#Crear las helper tables:

inscritos= db.Table('inscritos',
                  db.Column('materia_id', db.Integer, db.ForeignKey('materia.id'), primary_key = True),
                  db.Column('curso_id', db.Integer, db.ForeignKey('curso.id'), primary_key = True)
                 )

lista= db.Table('lista',
                  db.Column('alumno_id', db.Integer, db.ForeignKey('alumno.id'), primary_key = True),
                  db.Column('materia_id', db.Integer, db.ForeignKey('materia.id'), primary_key = True)
                 )

#modelos


    
class alumno(db.Model):
  
  id = db.Column('id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100))
  apellido = db.Column(db.String(100))
  fecha_nacimiento = db.Column(db.Date)
  grado = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable = False)
  materias = db.relationship('materia', secondary=lista, lazy = 'subquery', backref=db.backref('alumnos', lazy=True))
  notas = db.relationship('nota', backref='alumno', lazy=True)                      
  
  def __init__(self, nombre, apellido, fecha_nacimiento, grado):
    self.nombre = nombre
    self.apellido = apellido
    self.fecha_nacimiento = fecha_nacimiento
    self.grado = grado
                       
class curso(db.Model):

  id = db.Column('id', db.Integer, primary_key= True)
  nombre = db.Column(db.String(100))
  materias = db.relationship('materia', secondary=inscritos, lazy = 'subquery', backref=db.backref('cursos', lazy=True))
  alumnos = db.relationship('alumno', backref = 'curso', lazy = True)
  encargado = db.Column(db.Integer, db.ForeignKey('maestro.id'), nullable = False)

  def __init__(self, nombre, encargado):
    self.nombre = nombre
    self.encargado = encargado
                       
class materia(db.Model):
                       
  id = db.Column('id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100))
  maestro_id = db.Column(db.Integer, db.ForeignKey('maestro.id'), nullable = False)
  #cursos = db.relationship('curso', secondary=inscritos, lazy = 'subquery', backref=db.backref('materias', lazy=True))
  notas = db.relationship('nota', backref='materia', lazy=True)                      

  def __init__(self, nombre, maestro):
    self.nombre = nombre
    self.maestro = maestro
                       
class maestro(db.Model):
                       
  id = db.Column('id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100))
  apellido = db.Column(db.String(100))
  email = db.Column(db.String(150))
  encargado_cursos = db.relationship('curso', backref = 'maestro', lazy = True)
  materias = db.relationship('materia', backref = 'maestro', lazy = True)
  
  def __init__(self, nombre, apellido, email):
    self.nombre = nombre
    self.apellido = apellido
    self.email = email

class nota(db.Model):
  
  id = db.Column('id', db.Integer, primary_key = True)
  alumno_id = db.Column(db.Integer, db.ForeignKey('alumno.id'), nullable=False)
  materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)
  lab1 = db.Column('lab1', db.Integer)
  lab2 = db.Column('lab2', db.Integer)
  par1 = db.Column('par1', db.Integer)
  lab3 = db.Column('lab3', db.Integer)
  lab4 = db.Column('lab4', db.Integer)
  par2 = db.Column('par2', db.Integer)
  lab5 = db.Column('lab5', db.Integer)
  lab6 = db.Column('lab6', db.Integer)
  par3 = db.Column('par3', db.Integer)
  
  def __init__(self, alumno_id, materia_id, lab1 = 0, lab2 = 0, par1 = 0, lab3 = 0, lab4 = 0, par2 = 0, lab5 = 0, lab6 = 0, par3 = 0):
    self.alumno_id = alumno_id
    self.materia_id = materia_id
    self.lab1 = lab1
    self.lab2 = lab2
    self.par1 = par1
    self.lab3 = lab3
    self.lab4 = lab4
    self.par2 = par2
    self.lab5 = lab5
    self.lab6 = lab6
    self.par3 = par3  

#db.create_all()


#rutas

@d_app.route('/')
def view_index():
  return render_template('index.html')

@d_app.route('/home')
def view_home():  
  return render_template('home.html')


@d_app.route('/alumni/<int:alumniid>')
def view_alumni(alumniid):
  return render_template('alumni.html', alumni = alumno.query.filter_by(id = alumniid).first())

@d_app.route('/alumnis')
def view_alumnis():
  return render_template('alumnis.html', alumnis = alumno.query.all())


@d_app.route('/course')
def view_course():
  return render_template('course.html')

@d_app.route('/courses')
def view_courses():
  return render_template('courses.html')

@d_app.route('/newalumni', methods = ['GET', 'POST'])
def view_new_alumni():
  if request.method == 'POST':
    if not request.form['nombre'] or not request.form['apellido'] or not request.form['fecha'] or not request.form['grado']:
      flash('Por favor agregue todos los campos', 'error')
    else:      
      alumno_obj = alumno(request.form['nombre'],request.form['apellido'], date.fromisoformat(request.form['fecha']), request.form['grado'])
      db.session.add(alumno_obj)
      db.session.commit()
      flash('Alumno creado')      
      return redirect('/')  

  return render_template('create_alumni.html', grados = curso.query.all())

@d_app.route('/newcourse')
def view_new_course():
  return render_template('create_course.html')

@d_app.route('/newprofessor')
def view_new_professor():
  return render_template('create_professor.html')            

@d_app.route('/newsubject')
def view_new_subject():
  return render_template('create_subject.html')

@d_app.route('/login')
def view_login():
  return render_template('login.html')  

@d_app.route('/logout')
def view_logout():
  return render_template('logout.html')

@d_app.route('/professor')
def view_professor():
  return render_template('professor.html')

@d_app.route('/professors')
def view_professors():
  return render_template('professors.html')

@d_app.route('/subject')
def view_subject():
  return render_template('subject.html')

@d_app.route('/subjects')
def view_subjects():
  return render_template('subjects.html')
