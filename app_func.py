from flask import Flask
from flask import render_template
import funciones as f

app = Flask(__name__)
app.debug = True

@app.route("/")
def principal():
    return render_template('index.html')

@app.route("/artistas")
