from flask import render_template, Blueprint

bp_ventas = Blueprint("ventas", __name__)


@bp_ventas.route('/ventas/')
def ventas():
    return render_template("ventas/ventas.html")
