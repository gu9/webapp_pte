from application import app
from flask import render_template
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/contactus")
def contactus():
    return render_template("contact-page.html")

@app.route("/ielts")
def ielts():
    return render_template("coaching-sidebar-ielts.html")

@app.route("/generalenglish")
def generalenglish():
    return render_template("coaching-sidebar-english-speaking.html")

@app.route("/pte")
def pte():
    return render_template("coaching-sidebar-pte.html")
@app.route("/onlineclasses")
def onlineclasses():
    return render_template("online-classes.html")