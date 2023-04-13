from flask import render_template, Blueprint, redirect, request

bp_empleados = Blueprint("Empleados", __name__) #No debe tener el mismo nombre que la ruta Saludar
from SistemaArely.Sistema.modulos.empleados.model.empleados import EMPLEADOS

@bp_empleados.route('/empleados/')
def empleado(): #Debe llamarse distinto?
    # for clave,valor in EMPLEADOS.items(): # clave=variable, valor=valor de la variable, ejemplo:    clave=sexo, valor=H
        # print(f"{clave} = {valor}")
    cdx={
    "empleados":EMPLEADOS
    }
    return render_template("empleados/empleados.html", cdx=cdx)

@bp_empleados.route('/comentarios/<int:id>/') # < parámetro > indica una variable
def comentarios(id):
    empleado = EMPLEADOS.get(id)
    return empleado.get("comentarios")


@bp_empleados.route('/empleados/nuevo')
def nuevo():
    if request.method == 'GET':
        cdx = {
            'tipo': 'alta',
            'empleado': None
        }
        return render_template("empleados/empleados_nuevo.html", cdx=cdx)

    elif request.method == 'POST':
        cadena = ""
        nombre = request.form.get("nombre")
        direccion = request.form.get("direccion")
        telefono = request.form.get("telefono")
        nacimiento = request.form.get("nacimiento")
        mail = request.form.get("salario")
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")
        comentarios = request.form.get("comentarios")

        cadena += f"Nombre: {nombre}<br>"
        cadena += f"Direccion: {direccion}<br>"
        cadena += f"Telefono: {telefono}<br>"
        cadena += f"Fecha nac.: {nacimiento}<br>"
        cadena += f"Mail: {mail}<br>"
        cadena += f"Usuario: {usuario}<br>"
        cadena += f"Contrasena: {contrasena}<br>"
        cadena += f"Comentarios: {comentarios}<br>"

        llaves = EMPLEADOS.keys()
        llave_mayor = max(llaves)
        nuevo_empleado = {
            "nombre": "nombre",
            "direccion": "apellido",
            "telefono": "H",
            "nacimiento": 20,
            "mail": "comodin",
            "usuario": 15000,
            "contrasena": "",
            "comentarios": "<button>presioname</button>"
        }
        EMPLEADOS[llave_mayor + 1] = nuevo_empleado
        return redirect("/empleados/")
    else:
        return 'ERROR'


@bp_empleados.route('/borrar/<int:id>/')
def borrar(id):
    del(EMPLEADOS[id])
    return redirect("/empleados/")