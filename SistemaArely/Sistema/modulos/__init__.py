from flask import Flask

from SistemaArely.Sistema.modulos.home.views import bp_home
from SistemaArely.Sistema.modulos.empleados.views import bp_empleados
from SistemaArely.Sistema.modulos.ventas.views import bp_ventas

app = Flask(__name__)
app.register_blueprint(bp_home)
app.register_blueprint(bp_empleados)
app.register_blueprint(bp_ventas)
