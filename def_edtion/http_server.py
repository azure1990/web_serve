from flask import Flask, render_template, url_for
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



