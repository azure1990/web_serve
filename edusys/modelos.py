db = SQLAlchemy(app)

#Crear las helper tables:

cur_mat= db.Table('inscritos',
                  db.Column('materia_id', db.Integer, db.foreignKey('materia.id'), primary_key = True)
                  db.Column('curso_id', db.Integer, db.foreignKey('curso.id'), primary_key = True)
                 )

alu_mat= db.Table('notas',
                  db.Column('alumno_id', db.Integer, db.ForeignKey('alumno.id'), primary_key = True)
                  db.Column('materia_id', db.Integer, db.ForeignKey('materia.id'), primary_key = True)
                  db.Column('lab1', db.Integer),
                  db.Column('lab2', db.Integer),
                  db.Column('par1', db.Integer),
                  db.Column('lab3', db.Integer),
                  db.Column('lab4', db.Integer),
                  db.Column('par2', db.Integer),
                  db.Column('lab5', db.Integer),
                  db.Column('lab6', db.Integer),
                  db.Column('par3', db.Integer)
                 )

class alumno(db.Model):
  
  id = db.Column('alumno_id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100)
  apellido = db.Column(db.String(100)
  fecha_nacimiento = db.Column(db.Date)
  grado = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable = False)
  materias = db.relationship('materia', secondary=notas, lazy = 'subquery', bakckref=db.backref('alumnos', lazy=True))

class curso(db.Model):
                       
  id = db.Column('curso_id', db.Integer, primary_key= True)
  nombre = db.Column(db.String(100))
  materias = db.relationship('materia', secondary=inscritos, lazy = 'subquery', bakckref=db.backref('cursos', lazy=True))
  alumnos = db.relationship('alumno', backref = 'curso', lazy = true)
  encargado = db.Column(db.Integer, db.ForeignKey('maestro.id'), nullable = False)
                       
class materia(db.Model):
                       
  id = db.Column('materia_id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100))
  maestro = db.Column(db.Integer, db.ForeignKey('maestro.id'), nullable = False)
  #cursos = db.relationship('curso', secondary=inscritos, lazy = 'subquery', bakckref=db.backref('materias', lazy=True))

                       
class maestro(db.Model):
                       
  id = db.Column('maestro_id', db.Integer, primary_key = True)
  nombre = db.Column(db.String(100))
  apellido = db.Column(db.String(100))
  email = db.Column(db.String(150))
  encargado_cursos = db.relationship('curso', backref = 'maestro', lazy = true)
  materias = db.relationship('materia', backref = 'maestro', lazy = true)

  
