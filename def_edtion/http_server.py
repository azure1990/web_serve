from flask import Flask, render_template, url_for, request, redirect

d_app = Flask(__name__)
print(__name__)

@d_app('/')
def my_home():
  return render_template('index.html')
"""

@d_app('/about.html')
def about():
  return render_template('about.html')


@d_app('/works.html')
def work():
  return render_template('works.html')



@d_app('/contact.html')
def contact():
  return render_template('works.html')
"""


@d_app('/<string:page_name>')
def html_page(page_name):
  return render_template('page_name')

def write_to_file(data):
  with open("database.txt", mode='a') as database:
    email = data['email']
    subject = data['subject']
    message = data['message']
    file = database.write(f'\n{email},{subject},{message}')

@d_app('/submit_form', methods['POST', 'GET'])
def submit_form():
  if request.method=='POST':
    data = request.form.to_dict()
    write_to_file(data)
    return redirect('/thankyou.html')
  else:
    return "Something went wrong"
