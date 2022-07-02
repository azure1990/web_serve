db = SQLAlchemy(app)

#Crear las helper tables:

cur_mat= db.Table('inscritos',
                  db.Column('materia_id', db.Integer, db.foreignKey('materia.id'), primary_key = True)
                  db.Column('curso_id', db.Integer, db.foreignKey('curso.id'), primary_key = True)
                 )

alu_mat= db.Table('notas',
                  db.Column('alumno_id', db.Integer, db.ForeignKey('alumno.id'), primary_key = True)
                  db.Column('materia_id', db.Integer, db.ForeignKey('materia.id'), primary_key = True)
                 )

class nota():
  
  id = db.Column('id', db.Integer, primary_keyy = True)
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
  
    
class alumno(db.Model):
  
  id = db.Column('id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100)
  apellido = db.Column(db.String(100)
  fecha_nacimiento = db.Column(db.Date)
  grado = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable = False)
  materias = db.relationship('materia', secondary=notas, lazy = 'subquery', bakckref=db.backref('alumnos', lazy=True))
  notas = db.relationship('Nota', backref='alumno', lazy=True)                      
  
  def __init__(self, nombre, apellido, fecha_nacimiento, grado):
		self.nombre = nombre
    self.apellido = apellido
    self.fecha_nacimiento = fecha_nacimiento
    self.grado = grado
    self.materias = obtener segun grado y agregarlas con append. 
                       
class curso(db.Model):
                       
  id = db.Column('id', db.Integer, primary_key= True)
  nombre = db.Column(db.String(100))
  materias = db.relationship('materia', secondary=inscritos, lazy = 'subquery', bakckref=db.backref('cursos', lazy=True))
  alumnos = db.relationship('alumno', backref = 'curso', lazy = true)
  encargado = db.Column(db.Integer, db.ForeignKey('maestro.id'), nullable = False)
                       
class materia(db.Model):
                       
  id = db.Column('id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100))
  maestro = db.Column(db.Integer, db.ForeignKey('maestro.id'), nullable = False)
  #cursos = db.relationship('curso', secondary=inscritos, lazy = 'subquery', bakckref=db.backref('materias', lazy=True))
  notas = db.relationship('Nota', backref='materia', lazy=True)                      

                       
class maestro(db.Model):
                       
  id = db.Column('id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100))
  apellido = db.Column(db.String(100))
  email = db.Column(db.String(150))
  encargado_cursos = db.relationship('curso', backref = 'maestro', lazy = true)
  materias = db.relationship('materia', backref = 'maestro', lazy = true)

  
