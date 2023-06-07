from flask import Flask, jsonify, render_template
from controllers.eliminar_usuario import eliminar_usuario_bp
from controllers.registro_usuario import registrar_usuario_bp
from controllers.ver_productos import ver_productos_bp
from controllers.ver_status import ver_status_bp
from controllers.login import login_bp
from controllers.actualizar import actualizar_bp
from controllers.agregar import agregar_bp
from controllers.borrar import borrar_bp
from controllers.ver import ver_bp
from controllers.consultar_cliente import consultar_clientes_bp
from controllers.actualizar_usuario import actualizar_Cuenta_cliente_bp
from controllers.actualizar_contrasena_vendedor import actualizar_contrasena_vendedor_bp
from alchemyClasses.usuario import db

app = Flask(__name__)
app.register_blueprint(eliminar_usuario_bp)
app.register_blueprint(registrar_usuario_bp)
app.register_blueprint(ver_productos_bp)
app.register_blueprint(ver_status_bp)
app.register_blueprint(login_bp)
app.register_blueprint(actualizar_bp)
app.register_blueprint(agregar_bp)
app.register_blueprint(borrar_bp)
app.register_blueprint(ver_bp)
app.register_blueprint(consultar_clientes_bp)
app.register_blueprint(actualizar_Cuenta_cliente_bp)
app.register_blueprint(actualizar_contrasena_vendedor_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123pass@localhost:3306/bdd1'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
