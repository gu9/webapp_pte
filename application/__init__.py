from flask import Flask
from flask_mail import Mail
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRETKEY")
app.config["MAIL_SERVER"] = "smtp.hushmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("USER_MAIL")
app.config["MAIL_PASSWORD"] = os.environ.get("PASSWORD")
mail = Mail(app)
from application import routes
