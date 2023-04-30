from flask import render_template, redirect, flash, url_for
from readaholic import app, db, bcrypt
from readaholic.models import User
from readaholic.forms import AdminRegistrationForm, AdminLoginForm, DoAddBook

@app.route("/")
def home():
    # rendering(returning) html file(home.html) can see by view page source
    # web is a variable it can be any thing
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = AdminRegistrationForm()
    if form.validate_on_submit():  # send the infromation of register page on backend below three 3 lines
        # print(form.data)  #print data on back end if you want to see it 
        _email= form.data['email']  #  data(email) coming from register page now store in _email
        _password = form.data['password']
        _password = bcrypt.generate_password_hash(_password).decode("utf-8")
        # user is object variable of User
        user = User(email= _email, password=_password)    # passing data to User
        try:
            db.session.add(user)
            db.session.commit()
            # print( "user added") #print message if user added successfullly
            flash("you regiustered successfully, you may login now", "sussess")
            return redirect(url_for("login"))
        except:
            # print("fail to add user")
            flash(" somthing went wrong", "warning")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():  # to check whether data is there in data base
        _email =form.data['email']  # taking data from ligin form and assigne to variable
        _password = form.data['password']
        user = User.query.filter_by(email=_email).first() #checking  is user email similiar to variable. and return first email if more then one is same
        if not User:
            flash(f"No user with email{_email}fond reistered", "danger")
            return redirect(url_for("register"))
        else:
            if bcrypt.check_password_hash(user.password, _password):
                flash("you log in successfully", "success")
                return redirect(url_for("home"))
            else:
                flash("you entered wrong password", "danger")

    return render_template("login.html", form=form)

@app.route("/Addbook", methods=["GET", "POST"] )
def Addbook():
    form = DoAddBook()
    return render_template("Addbook.html", form=form)
