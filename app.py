from flask import Flask, render_template
from os import system
import conexion as conn

app = Flask(__name__)

db = conn.DB()
system("clear")

## agregar 
def create():
    name = str(input("INGRESA SU NOMBRE: "))
    email = str(input("INGRESA SU EMAIL: "))
    if(len(name) > 0 and len(email) > 0):
        sql = "INSERT INTO sistema(name,email) VALUES(?,?)"
        parametros = (name,email)
        db.ejecutar_consulta(sql,parametros)
        print("Insertados")

## listar
def read():
    sql = "SELECT * FROM sistema"
    result = db.ejecutar_consulta(sql)
    for data in result:
        print(""" 
        ID :        {}
        NOMBRE :    {}
        EMAIL :     {}
        """.format(data[0],data[1],data[2]))

## modificar
def update():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
        name = str(input("INGRESA SU NOMBRE: "))
        email = str(input("INGRESA SU EMAIL: "))
        if(len(name) > 0 and len(email) > 0):
            sql = "UPDATE sistema SET name=?,email=? WHERE id=?"
            parametros = (name,email,id)
            db.ejecutar_consulta(sql,parametros)
            print("Actualizado!")
    else:
        print("Se require un ID")

## eliminar
def delete():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
        sql = "DELETE FROM sistema WHERE id=?"
        parametros = (id,)
        db.ejecutar_consulta(sql,parametros)
        print("Eliminado del sistema con exito.")
    else:
        print("Se require un ID")

## buscar
def search():
    nombre = str(input("Buscar por nombre: "))
    if(len(nombre) > 0):
        sql = "SELECT * FROM sistema WHERE name LIKE ?"
        parametros = ('%{}%'.format(nombre),)
        result = db.ejecutar_consulta(sql,parametros)
        for data in result:
            print(""" 
            +ID :        {}
            +NOMBRE :    {}
            +EMAIL :     {}""".format(data[0],data[1],data[2]))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/listar')
def listar():
    return render_template("listar.html")

@app.route('/agregar')
def agregar():
    return render_template("agregar.html")

@app.route('/eliminar')
def eliminar():
    return render_template("eliminar.html")

@app.route('/modificar')
def buscar():
    return render_template("buscar.html")

@app.route('/buscar')
def modificar():
    return render_template("modificar.html")

app.run(port=5000, debug=True)