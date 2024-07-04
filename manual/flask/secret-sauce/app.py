from flask import Flask
from os import environ

app = Flask(__name__)

sauce = environ.get('SECRET_SAUCE')

@app.route("/")
def index():
    if sauce:
        return f"The secret sauce is: {sauce}!"
    else:
        return "You'll never find my secret sauce."