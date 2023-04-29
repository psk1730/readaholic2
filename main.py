from flask import Flask, render_template
from forms import AdminRegistrationForm, AdminLoginForm, DoAddBook

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key_33'

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
