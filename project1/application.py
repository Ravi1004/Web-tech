import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://yainmriqptbdia:ef9eb65b36e26462fab4fa3190ea7982f65a5b450e7be9789b4ac2f507b8f634@ec2-54-81-37-115.compute-1.amazonaws.com:5432/d226orf1s2l1ac"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
db.init_app(app)

with app.app_context():
    db.create_all()

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def registration():

    return render_template("registration.html")


@app.route("/registration", methods=["POST"])
def browser():
    Firstname = request.form.get("fname")
    Lastname = request.form.get("lname")
    Name = Firstname+" "+Lastname
    username = request.form.get("uname")
    password = request.form.get("pass")
    credentials = User(username=username, password=password)
    db.session.add(credentials)
    db.session.commit()
    # s = "Hello " + Firstname + " " + Lastname + ": Your Username is " + username
    return render_template("registered.html", message=Name + ", account is sucessfully registered.")


@app.route("/admin")
def admin():
    users = User.query.order_by("user_created_on").all()
    return render_template("admin.html", users=users)

# def main():
#     with app.app_context():
#         db.create_all()
#         print("tables created")


# if _name_ == "_main_":
#     with app.app_context():
#         main()
