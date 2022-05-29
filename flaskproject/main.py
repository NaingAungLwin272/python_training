import os
import pymysql
from flask import Flask, flash, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask import jsonify
from app import app
from db import mysql
from flask import send_file
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
app.secret_key = 'the random string'


@app.route('/', methods=['GET', 'POST'])
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

                return redirect(url_for('dashboard', account=account))
            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Email or Password is Incorrect'

    return render_template('login.html', loginerror=loginerror, msg=msg)


@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


@app.route('/users/userpost')
def user_post():
    return render_template('user_post.html')


@ app.route('/users', methods=['POST', 'GET'])
def users():
    erroruser = None
    erroremail = None
    errorpass = None
    errorconpass = None
    erroraddress = None
    conpasserror = None
    passerror = None
    phoneerror = None
    errorphone = None
    errordob = None

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmpass = request.form.get('confirmpass')
        type = request.form.get('user')
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
        session["user"] = type

        if name == '':
            erroruser = 'User input Can`t be blank'

        if email == '':
            erroremail = 'Email input Can`t be blank'

        if password == '':
            passerror = 'Password input Can`t be blank'

        if confirmpass == '':
            conpasserror = 'Confirm Password input Can`t be blank'

        if phone == '':
            errorphone = 'Phone input Can`t be blank'

        if dob == '':
            errordob = 'Date of Birth Can`t be blank'

        if address == '':
            erroraddress = 'Address input Can`t be blank'

        if len(password) < 8:
            errorpass = 'Password must be at least 8 characters '
        if confirmpass not in password:
            errorconpass = 'Confirmpassword and Password must be same'
        if len(phone) > 11 or len(phone) < 11:
            phoneerror = 'Phone can`t be greather than 11 and less than 11 '
        if not phone.isdigit():
            phoneerror = 'Phone must be number'

        elif not any(char.isupper() for char in password):
            errorpass = 'Password should have at least one uppercase letter'

        elif not any(char.isdigit() for char in password):
            errorpass = 'Password should have at least one numeral'

        else:
            if profile.filename == '':
                flash('No selected file')

            else:
                profile.save(os.path.join(
                    "../flaskproject/profile/", profile.filename))

            return redirect(url_for('user_confirm', name=name, email=email, password=password, phone=phone, dob=dob, address=address, profile=profile, type=type))
    return render_template('user.html', erroruser=erroruser, erroremail=erroremail, errorpass=errorpass, passerror=passerror, errorconpass=errorconpass, conpasserror=conpasserror, phoneerror=phoneerror, errorphone=errorphone, erroraddress=erroraddress, errordob=errordob)


@app.route('/users/userconfirm', methods=['GET', 'POST'])
def user_confirm():
    now = datetime.datetime.now()
    name = session.get("name")
    email = session.get("email")
    password = session.get("password")
    phone = session.get("phone")
    dob = session.get("dob")
    address = session.get("address")
    profile = request.args.get('profile')
    type = request.args.get("type")
    hashed_password = generate_password_hash(password)

    if request.method == 'POST':

        sql = "INSERT INTO users(name, email, password, phone, address, dob, profile, created_at, updated_at, type)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (name, email, hashed_password, phone,
                address, dob, profile, now, now, type)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('user_list'))
    return render_template('user_confirm.html', name=name, email=email, hashed_password=hashed_password, phone=phone, dob=dob, address=address, profile=profile, type=type)


@app.route('/users/userlists')
def user_list():

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    data = cursor.fetchall()

    return render_template('user_list.html', data=data)


@app.route('/users/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    erroruser = None
    erroremail = None
    errorphone = None
    erroraddress = None
    errordob = None
    phoneerror = None

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id))
    data = cursor.fetchall()
    conn.close()
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        type = request.form.get('user')
        phone = request.form.get('phone')
        dob = request.form.get('dob')
        address = request.form.get('address')

        session["id"] = id

        session["name"] = name
        session["email"] = email

        session["phone"] = phone
        session["dob"] = dob
        session["address"] = address
        session["user"] = type
        if name == '':
            erroruser = 'User Input Can`t be blank'
        if email == '':
            erroremail = 'Email Input Can`t be blank'
        if phone == '':
            errorphone = 'Phone Input Can`t be blank'
        if dob == '':
            errordob = 'Date of Birth Can`t be blank'
        if address == '':
            erroraddress = 'Address input Can`t be blank'
        if not phone.isdigit():
            phoneerror = 'Phone must be number'
        elif len(phone) > 11 or len(phone) < 11:
            phoneerror = 'Phone can`t be greather than 11 and less than 11 '

        else:

            return redirect(url_for('userup_confirm', name=name, email=email, dob=dob, address=address, type=type, phone=phone))
    return render_template("user_update.html", erroruser=erroruser, erroremail=erroremail, errorphone=errorphone, errordob=errordob, erroraddress=erroraddress, phoneerror=phoneerror, data=data)


@app.route('/users/userupdateconfirm/', methods=['GET', 'POST'])
def userup_confirm():
    id = session.get("id")
    name = session.get("name")
    email = session.get("email")
    type = session.get("user")
    dob = session.get("dob")
    phone = session.get("phone")
    address = session.get("address")

    if request.method == 'POST':

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET name = %s, email = %s, phone = %s,address = %s, dob = %s, type = %s WHERE id = %s", (name, email, phone, address, dob, type, id))
        conn.commit()
        conn.close()
        return redirect(url_for('user_list'))
    return render_template('user_update_confirm.html', name=name, email=email, phone=phone, address=address, dob=dob, type=type, id=id)


@app.route('/duser')
def d_user():
    return render_template('user_delete.html')


@app.route('/users/deleteuser/<int:id>', methods=['GET', 'POST'])
def deleteuser(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id))
    data = cursor.fetchall()
    conn.close()
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        type = request.form.get('user')
        phone = request.form.get('phone')
        dob = request.form.get('dob')
        address = request.form.get('address')

        session["id"] = id

        session["name"] = name
        session["email"] = email

        session["phone"] = phone
        session["dob"] = dob
        session["address"] = address
        session["user"] = type

        return redirect(url_for('d_user'))
    return render_template("user_delete.html", data=data)


if __name__ == 'main':
    app.run(debug=True)
