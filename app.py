from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return "Welcome"

@app.route('/welcome/home')
def say_welcomeHome():
    return "Welcome to the Home"

@app.route('/welcome/back')
def say_welcomeBack():
    return "Welcome Back"
