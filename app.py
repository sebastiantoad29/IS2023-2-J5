from flask import Flask, redirect, url_for
from alchemyClasses.__init__ import db
from alchemyClasses.vendedor import Vendedor
from controllers.agregar import agregar_bp
from controllers.borrar import borrar_bp
from controllers.ver import ver_bp
from controllers.actualizar import actualizar_bp

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Starmoon66680@localhost:3306/doñabd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'S12'

db.init_app(app)

app.register_blueprint(agregar_bp)
app.register_blueprint(borrar_bp)
app.register_blueprint(ver_bp)
app.register_blueprint(actualizar_bp)

@app.route('/')
def inicio():
    return redirect(url_for('agregar.agregar_vendedor'))

if _name_ == '_main_':
    app.run(port=3000, debug=True)