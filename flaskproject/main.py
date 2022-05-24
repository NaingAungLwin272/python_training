import os
import pymysql
from flask import Flask, flash, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask import jsonify
from app import app
from db import mysql
from flask import send_file
import datetime
app.secret_key = 'the random string'


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/logins', methods=['GET', 'POST'])
def login_post():
    loginerror = None
    msg = None
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = mysql.connect()
        cursor = conn.cursor()
        if password == '' or email == '':
            loginerror = 'Input Can`t be blank'
        else:
            cursor.execute(
                'SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
            account = cursor.fetchone()
            if account:

                return redirect(url_for('user_post', account=account))
            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Email or Password is Incorrect'

    return render_template('login.html', loginerror=loginerror, msg=msg)


@app.route('/users/userpost')
def user_post():
    return render_template('user_post.html')


@ app.route('/users', methods=['POST', 'GET'])
def users():
    error = None
    errorpass = None
    phoneerror = None

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmpass = request.form.get('confirmpass')
        # usertypes = detail['user']
        phone = request.form.get('phone')
        dob = request.form.get('dob')
        address = request.form.get('address')
        profile = request.files['profile']

        session["name"] = name
        session["email"] = email
        session["password"] = password
        session["phone"] = phone
        session["dob"] = dob
        session["address"] = address

        if name == '' or email == '' or password == '' or phone == '' or dob == '' or address == '':
            error = 'Input can`t be blank'

        elif len(password) < 8:
            errorpass = 'Password must be at least 8 characters '
        elif not any(char.isupper() for char in password):
            errorpass = 'Password should have at least one uppercase letter'
        elif not any(char.isdigit() for char in password):
            errorpass = 'Password should have at least one numeral'
        elif confirmpass not in password:
            errorpass = 'Confirmpassword and Password must be same'
        elif not phone.isdigit():
            phoneerror = 'Phone must be number'
        elif len(phone) > 13:
            phoneerror = 'Phone can`t be greather than 8 '
        else:
            if profile.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:
                profile.save(os.path.join(
                    "../flaskproject/profile/", profile.filename))

            return redirect(url_for('user_confirm', name=name, email=email, password=password, phone=phone, dob=dob, address=address, profile=profile))
    return render_template('user.html', error=error, errorpass=errorpass, phoneerror=phoneerror)


@ app.route('/users/userconfirm', methods=['GET', 'POST'])
def user_confirm():
    now = datetime.datetime.now()
    name = session.get("name")
    email = session.get("email")
    password = session.get("password")
    phone = session.get("phone")
    dob = session.get("dob")
    address = session.get("address")
    profile = request.args.get('profile')

    if request.method == 'POST':

        sql = "INSERT INTO users(name, email, password, phone, address, dob, profile, created_at, updated_at)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (name, email, password, phone, address, dob, profile, now, now)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('user_list'))
    return render_template('user_confirm.html', name=name, email=email, password=password, phone=phone, dob=dob, address=address, profile=profile)


@ app.route('/users/userlist')
def user_list():

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    data = cursor.fetchall()
    return render_template('user_list.html', data=data)


if __name__ == 'main':
    app.run(debug=True)
