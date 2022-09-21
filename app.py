from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

def listar():
    return render_template("listar.html")

def agregar():
    return render_template("agregar.html")

def eliminar():
    return render_template("eliminar.html")

def buscar():
    return render_template("buscar.html")

def modificar():
    return render_template("modificar.html")

app.run(port=5000, debug=True)