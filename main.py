from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask API is running'


@app.route('/sum')
def sum():
    return 'this is sum method'