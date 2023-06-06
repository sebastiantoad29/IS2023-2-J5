from flask import Flask, jsonify
from controllers.eliminar_usuario import eliminar_usuario_bp
from controllers.registro_usuario import registrar_usuario_bp
from controllers.ver_productos import ver_productos_bp
from alchemyClasses.usuario import db

app = Flask(__name__)
app.register_blueprint(eliminar_usuario_bp)
app.register_blueprint(registrar_usuario_bp)
app.register_blueprint(ver_productos_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123pass@localhost:3306/new'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
