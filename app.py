from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Estamos en la demo 2.0!!!'
