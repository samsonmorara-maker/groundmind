from app import app
from flask import render_template

posts=[
    {"id":1 , "title":"Can AI master the Perfect Lawn?","excerpt":"Universal Autonomous Robotic Lawn Mowe", "content":"A next-generation, wire-free, GPS-free lawn-care system engineered to adapt seamlessly to any outdoor environment"},
    {"id":2 , "title":"Can AI master the Perfect Lawn?","excerpt":"Universal Autonomous Robotic Lawn Mowe", "content":"A next-generation, wire-free, GPS-free lawn-care system engineered to adapt seamlessly to any outdoor environment"},
    {"id":3 , "title":"Can AI master the Perfect Lawn?","excerpt":"Universal Autonomous Robotic Lawn Mowe", "content":"A next-generation, wire-free, GPS-free lawn-care system engineered to adapt seamlessly to any outdoor environment"}
]

@app.route("/")
def home ():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
