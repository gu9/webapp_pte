from application import app
from application import mail
from flask import render_template, redirect, flash, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired
from flask_mail import Mail,Message
OUR_CHOICES = ['PTE', 'IELTS', 'Spoken English', 'General English']

class ContactUs(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject")
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


class FreeAssesment(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    mobileno = StringField("mobileno", validators=[DataRequired()])
    choose = SelectField('choose', choices=OUR_CHOICES)
    message = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("submitnow")


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route('/handle_form_data', methods=['POST'])
def handle_form_data():
    yourname = request.form.get("yourname")
    email = request.form.get("email")
    mobileno = request.form.get("mobileno")
    message = request.form.get("message")
    msg = Message("Free Assessment",
                  sender="harpreetpte@hushmail.com",
                  recipients=[email])
    msg.body = """From: %s <%s>%s %s""" % (yourname, email, message, mobileno)
    mail.send(msg)
    flash("You have successfully submitted query!")
    return redirect(url_for("index"))


@app.route("/contactus",methods=['GET','POST'])
def contactus():
    form = ContactUs()
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        phone = form.phone.data
        subject = form.subject.data
        message = form.message.data
        msg = Message(subject,
                      sender="harpreetpte@hushmail.com",
                      recipients=[email])
        msg.body = """From: %s <%s>%s %s"""%(name, email, message, phone)
        mail.send(msg)
        flash("You have successfully submitted query!")
        return redirect(url_for("index"))
    return render_template("contact-page.html", form=form)

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

@app.route("/videotestimonials")
def videotestimonials():
    return render_template("video-testimonial-page.html")