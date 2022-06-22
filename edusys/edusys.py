from flask import Flask, render_template, url_for, request, redirect

d_app = Flask(__name__)


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
"""
@d_app.route('/thankyou.html')
def love():
  return render_template('thankyou.html')



@d_app('/about.html')
def about():
  return render_template('about.html')


@d_app('/works.html')
def work():
  return render_template('works.html')



@d_app('/contact.html')
def contact():
  return render_template('works.html')



@d_app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name)

def write_to_file(data):
  with open("database.txt", mode='a') as database:
    email = data['email']
    subject = data['subject']
    message = data['message']
    file = database.write(f"{email},{subject},{message}"")


def write_to_file(data):
  with open("database.txt", mode='a') as database:
    file = database.write(f'{data}')

@d_app.route('/submit_form', methods = ['POST', 'GET'])
def submit_f():
  if request.method=='POST':
    data = request.form.to_dict()
    write_to_file(data)
    return redirect('/thankyou.html')
  else:
    return "Something went wrong"

"""
