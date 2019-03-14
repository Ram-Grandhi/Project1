from flask import Flask, render_template  # imports flask webserver
import datetime

app = Flask(__name__)


@app.route("/")  # route is part of url to determine which page to open. / is the default page.
# When you write function under this decorator, here meaning when you go to default page, this function runs
def index():
    return "hello world"


@app.route("/ram")  # Route need not be same as function name
def test():
    return "Hello Ram!!!"


@app.route("/<string:name>")  # This is a template, any string after / is stored in variable name pass to hello
def hello(name):
    name=name.capitalize()
    return f"<h1>Hello, {name}</h1>"  # f is for format.


@app.route("/page")
def page():
    return render_template("Hello.html")  # Hello.html should be placed in templates folder


@app.route("/page2")
def page2():
    headline = "Good Bye!!!"
    return render_template("Hello1.html",headline=headline)
    # Passing this variable using {{}} is jinga2 and flask takes care of it


@app.route("/newyear")
def is_new_year():
    now = datetime.datetime.now()
    newyear = now.month == 1 and now.day == 1
    # newyear = True
    return render_template("hello1.html", newyear=newyear)


app.run(port=5000)

# To run execute set FLASK_APP=filename.py
# In linux, export FLASK_APP=filename.py
