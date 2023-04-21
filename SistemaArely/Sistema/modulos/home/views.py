
from flask import render_template, Blueprint, request

bp_home = Blueprint("home", __name__) #No debe tener el mismo nombre que la ruta Saludar

@bp_home.route('/')
def home():
    return render_template("home/index.html")

@bp_home.route('/inicio/')
def inicio():
    return render_template("home/inicio.html")

@bp_home.route('/sesion/', methods =['GET','POST'])
def sesion():
    return render_template("home/index.html")
    #usuario = request.form.get("usuario")
    #contra = request.form.get("contra")
    #print(usuario)
    #print(contra)

    #if (usuario == 'admin' & contra == '123'):
