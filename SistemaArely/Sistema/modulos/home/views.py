from flask import render_template, Blueprint

bp_home = Blueprint("home", __name__) #No debe tener el mismo nombre que la ruta Saludar

@bp_home.route('/')
def home():
    return render_template("home/index.html")