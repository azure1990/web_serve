@d_app.route('/')
def view_index():
  return render_template('index.html')

@d_app.route('/home')
def view_home():  
  return render_template('home.html')


@d_app.route('/alumni')
def view_alumni():
  return render_template('alumni.html')

@d_app.route('/alumnis')
def view_alumnis():
  return render_template('alumnis.html')

@d_app.route('/course')
def view_course():
  return render_template('course.html')

@d_app.route('/courses')
def view_courses():
  return render_template('courses.html')

@d_app.route('/newalumni')
def vieW_new_alumni():
  return render_template('create_alumni.html')

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