from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#db = SQLAlchemy()
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@localhost/db_name"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'dev'
#db.init_app(app)

Consultar_info_clientes_Admin_bp = Blueprint('Consultar_info_clientes_Admin', __name__, url_prefix='/Consultar_info_clientes_Admin')


class Administrador(db.Model):
    id_admin = db.Column(db.String(200), primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellidoP = db.Column(db.String(45), nullable=False)
    apellidoM = db.Column(db.String(45), nullable=False)

    # Datos necesarios del administrador


class Usuario(db.Model):
    id_usuario = db.Column('id_usuario', db.INTEGER, primary_key=True)
    nombre = db.Column('nombre', db.String(50))
    apellidoP = db.Column('apellidoP', db.String(50))
    apellidoM = db.Column('apellidoM', db.String(50))
    edad = db.Column('edad', db.INTEGER, primary_key=True)
    email = db.Column('email', db.String(100))
    telefono = db.Column('telefono', db.String(20))

    # Datos del usuario reelevantes o necesarios


@app.route('/administrador/<string:admin_id>/clientes')
def consultar_clientes(admin_id):
    administrador = Administrador.query.get(admin_id)
    if not administrador:
        return render_template('error_admin_consulta.html', mensaje='Administrador no encontrado')

    clientes = Usuario.query.all()
    if not clientes:
        return render_template('error_admin_consulta.html', mensaje='No hay clientes registrados')

    return render_template('BusquedaCliente_admin.html', administrador=administrador, clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
