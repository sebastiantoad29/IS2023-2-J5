from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#db = SQLAlchemy()
#app.config[
#    'SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@localhost/db_name"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'dev'
#db.init_app(app)

Consultar_info_clientes_vendedor_bp = Blueprint('Consultar_info_clientes_vendedor', __name__, url_prefix='/Consultar_info_clientes_vendedor')


class Vendedor(db.Model):
    id_vendedor = db.Column('Vendedor;', db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidoP = db.Column(db.String(50), nullable=False)
    apellidoM = db.Column(db.String(50), nullable=False)

    # Datos del Vendedor reelevantes


class Usuario(db.Model):
    id_usuario = db.Column('id_usuario', db.INTEGER, primary_key=True)
    nombre = db.Column('nombre', db.String(50))
    apellidoP = db.Column('apellidoP', db.String(50))
    apellidoM = db.Column('apellidoM', db.String(50))
    edad = db.Column('edad', db.INTEGER, primary_key=True)
    email = db.Column('email', db.String(100))
    telefono = db.Column('telefono', db.String(20))

    # Datos del usuario reelevantes o necesarios


class AtenderPedido(db.Model):
    pedido_id = db.Column('numero de pedido', db.Integer, primary_key=True)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedor.id_vendedor'))

    # Datos reelevantes de los pedidos realizados


class GenerarReporte(bd.Model):
    reporte_id = db.Column('reporte de venta', db.Integer)

    #Datos reelevantes del reporte generado por venta


@app.route('/vendedor/<int:vendedor_id>/clientes')
def consultar_clientes(vendedor_id):
    vendedor = Vendedor.query.get(vendedor_id)
    if not vendedor:
        return render_template('ErrorBusqueda.html', mensaje='Vendedor no encontrado')

    atender_pedidos = AtenderPedido.query.filter_by(vendedor_id=vendedor_id).all()
    if not atender_pedidos:
        return render_template('ErrorBusqueda.html', mensaje='No se encuentran clientes atendidos por este vendedor')

    cliente_ids = [atender_pedido.pedido_id for atender_pedido in atender_pedidos]
    clientes = Usuario.query.filter(Usuario.id_usuario.in_(cliente_ids)).all()

    return render_template('BusquedaCliente_vendedor.html', vendedor=vendedor, clientes=clientes)


if __name__ == '__main__':
    app.run(debug=True)