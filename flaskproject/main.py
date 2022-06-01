from werkzeug.routing import BaseConverter
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
        cursor.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()

        if password == '' or email == '':
            loginerror = 'Input Can`t be blank'
        else:

            if account[11] == '1':
                session["loggedin"] = True
                session["ids"] = account[0]
                session["emailemail"] = account[2]

                return redirect(url_for('admin_dash'))
            elif account[11] == '0':
                session["loggedin"] = True
                session["id"] = account[0]
                session["emailemail"] = account[2]

                return redirect(url_for('user_dash'))
            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Email or Password is Incorrect'

    return render_template('login.html', loginerror=loginerror, msg=msg)


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('ids', None)
    session.pop('email', None)
    # Redirect to login page
    return redirect(url_for('login_post'))


@app.route('/userdash')
def user_dash():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('userdashboard.html', emails=session["emailemail"])

    return redirect(url_for('login_post'))


@app.route('/admindash')
def admin_dash():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('admindashboard.html', emails=session["emailemail"])

    return redirect(url_for('login_post'))


@app.route('/profile', methods=['GET', 'POST'])
def login_profile():

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (session["id"]))
    account = cursor.fetchone()
    return render_template('loginprofile.html', account=account)


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

        return redirect(url_for('user_lists'))
    return render_template('user_confirm.html', name=name, email=email, hashed_password=hashed_password, phone=phone, dob=dob, address=address, profile=profile, type=type)


@app.route("/users/userlists/")
def user_lists():
    users = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        users.append({"id": row[0], "name": row[1],
                     "email": row[2], "phone": row[4], "address": row[5], "dob": row[6], "created_at": row[8], "updated_at": row[9], "type": row[11]})
    conn.close()
    return render_template("user_list.html", users=users)


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


@app.route('/users/updatepassword', methods=['GET,POST'])
def user_uppass():
    return render_template('')


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
        return redirect(url_for('user_lists'))
    return render_template('user_update_confirm.html', name=name, email=email, phone=phone, address=address, dob=dob, type=type, id=id)


@app.route('/deleteuser/<int:id>')
def deleteuser(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id))
    conn.commit()
    conn.close()
    return redirect(url_for('user_lists'))


@app.route('/posts/', methods=['GET', 'POST'])
def post_create():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')

        session['title'] = title
        session['desc'] = desc
        return redirect(url_for('postconfirm', title=title, desc=desc))
    return render_template('post_create.html')


@app.route('/posts/postconfirm/', methods=['GET', 'POST'])
def postconfirm():
    now = datetime.datetime.now()
    title = session.get("title")

    desc = session.get("desc")

    if request.method == 'POST':

        sql = "INSERT INTO posts(title,created_at,updated_at,description)VALUES(%s, %s, %s, %s)"
        data = (title, now, now, desc)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('post_lists'))
    return render_template('post_confirm.html', title=title, desc=desc)


@app.route("/posts/postlists/")
def post_lists():

    search = request.args.get('search')
    connect = mysql.connect()
    cursors = connect.cursor()
    cursors.execute(
        "SELECT title,description FROM posts WHERE title LIKE %s OR description LIKE %s", (search, search))
    data = cursors.fetchall()
    posts = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    for row in cursor.fetchall():
        posts.append({"id": row[0], "title": row[1],
                     "status": row[2], "created_at": row[3], "updated_at": row[4], "description": row[5]})
    conn.close()
    return render_template("post_list.html", posts=posts, data=data)


@app.route("/posts/<int:id>", methods=['GET', 'POST'])
def postupdate(id):

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE id = %s", (id))
    posts = cursor.fetchall()
    conn.close()
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')

        session["id"] = id
        session['title'] = title
        session['desc'] = desc

        return redirect(url_for('postup_confirm', title=title, desc=desc))
    return render_template("post_update.html", posts=posts)


@app.route('/posts/postupdateconfirm/', methods=['GET', 'POST'])
def postup_confirm():
    id = session.get("id")
    title = session.get("title")
    desc = session.get("desc")

    if request.method == 'POST':

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE posts SET title = %s, description = %s WHERE id = %s", (title, desc, id))
        conn.commit()
        conn.close()
        return redirect(url_for('post_lists'))
    return render_template('post_update_confirm.html', title=title, desc=desc, id=id)


# @app.route('/search', methods=['GET', 'POST'])
# def post_search():
#
#    search = '%' + request.args.get('search') + '%'
#
#    return redirect(url_for('post_lists', data=data))


@app.route('/deletepost/<int:id>')
def deletepost(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts WHERE id = %s", (id))
    conn.commit()
    conn.close()
    return redirect(url_for('post_lists'))


if __name__ == 'main':
    app.run(debug=True)
