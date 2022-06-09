from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/login', methods=['Post'])
def receive_data():
    name = request.form['username'],
    password = request.form['password']
    return f"<h1>name:{name}, password:{password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)