from flask import Flask, render_template
from forms import AdminRegistrationForm, AdminLoginForm, DoAddBook
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key_33'
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///site.db"
# data base that you created
db = SQLAlchemy(app)


class User(db.Model):     # model or data base 
    id = db.Column(db.Integer, primary_key = True)   # to tell that no two be of same id
    email = db.Column(db.String(60), nullable= False)
    password = db.Column(db.String(32), nullable = False)

    def __reper__(self):
        return f"User(email: {self.email})"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(120), nullable= False)  #title is must
    isbn = db.Column(db.Integer, unique= True, nullable= False)
    shop_link = db.Column(db.String(120), nullable= True)  #optional
    author = db.Column(db.String(60), nullable = False)
    gener = db.Column(db.String(60), nullable= False)
    rating= db.Column(db.Float, nullable= False)
    image = db.Column(db.String(120), nullable = True, default= "default.jpg")
    tiny_summry = db.Column(db.Text, nullable = False)
    def __reper__(self):
        return f"Book(title: {self.title}, isbn:{ self.isbn})"

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
        print("success")
        # print(form.data)  #print data on back end if you want to see it 
        _email= form.data['email']  #  data(email) coming from register page now store in _email
        _password = form.data['password']
        # user is object variable of User
        user = User(email= _email, password=_password)    # passing data to User
        db.session.add(user)
        db.session.commit()
        # print( "user added")
    return render_template("register.html", form=form)

@app.route("/login")
def login():
    form = AdminLoginForm()
    return render_template("login.html", form=form)

@app.route("/Addbook", methods=["GET", "POST"] )
def Addbook():
    form = DoAddBook()
    return render_template("Addbook.html", form=form)
    



if __name__ == "__main__":
    app.run(debug=True)
