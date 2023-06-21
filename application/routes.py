from application import app, get_db
from flask import render_template, request, redirect, url_for, session
from application import database_helpers
from application.models import User


def transform_tuples_to_user_classes(users):
    users_as_class = []
    for user in users:
        user_class_object = User(id=user[0], first_name=user[1], last_name=user[2], dob=user[3], phone_number=user[4], email=user[5], password=user[6])
        users_as_class.append(user_class_object)
    return users_as_class


@app.route('/')
@app.route('/home')
def home_page():

    return render_template("home.html")

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/registration', methods=("GET", "POST"))
def add_user():
    if request.method == "POST":
        print(f"Added New User: {request.form}")
        name = request.form['name']
        last_name = request.form['last_name']
        dob = request.form['birth_date']
        phone_number = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        
        connection = get_db()
        database_helpers.add_new_user(db=connection,
                                        first_name=name,
                                        last_name=last_name,
                                        birth_date=dob,
                                        phone=phone_number,
                                        email=email,
                                        password=password)
        
        return redirect(url_for('home_page'))
    return render_template("registration.html")

@app.route('/login', methods=("GET", "POST"))
def user_login():
    if request.method == "POST":
        print(f"Tries To Log In: {request.form}")
        email, password = request.form['email'], request.form['password']
        connection = get_db()
        user = database_helpers.get_all_users(db=connection, email=email, password=password)
        if user is None:
            return render_template("login.html", log_in_warning="User Doesn't Exist!")
        print(f"User Logged In: {user}")
        user = User(user[0], user[1], user[2], user[3], user[4], user[5])
        session['id'] = user.id
        session['name'] = user.name
        session['last_name'] = user.last_name
        
        return redirect(url_for('home_page'))
    return render_template('login.html')

@app.route('/logout', methods=("GET", "POST"))
def user_logout():
    session.clear()
    return render_template('login.html')