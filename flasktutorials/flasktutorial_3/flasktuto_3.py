
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return 'Welcome'


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmpword = request.form['confirmpassword']
        if username == '' or password == '' or email == '' or confirmpword == '':
            error = 'Input Can`t be blank'
        else:
            return redirect(url_for('welcome'))
    return render_template('index.html', error=error)


app.run()
