from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#db = SQLAlchemy()
#app.config[
#    'SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@localhost/db_name"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'dev'
#db.init_app(app)

Actualizar_Cuenta_cliente_bp = Blueprint('Actualizar_Cuenta_cliente', __name__, url_prefix='/Actualizar_Cuenta_cliente')


class Usuario(db.Model):
    id_usuario = db.Column('id_usuario', db.INTEGER, primary_key=True)
    nombre = db.Column('nombre', db.String(50))
    apellidoP = db.Column('apellidoP', db.String(50))
    apellidoM = db.Column('apellidoM', db.String(50))
    edad = db.Column('edad', db.INTEGER, primary_key=True)
    email = db.Column('email', db.String(100))
    password = db.Column('password', db.String(100))
    telefono = db.Column('telefono', db.String(20))

    # Datos del usuario reelevantes o necesarios


@app.route('/cliente/<int:cliente_id>/editar', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    cliente = Usuario.query.get(cliente_id)
    if not cliente:
        return render_template('error_actualizar_cuenta_cliente.html', mensaje='Cliente no encontrado')

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.apellidoP = request.form['apellidoP']
        cliente.apellidoM = request.form['apellidoM']
        cliente.edad = request.form['edad']
        cliente.email = request.form['email']
        cliente.password = request.form['password']
        cliente.telefono = request.form['telefono']

        # Actualizar los campos de los datos del cliente

        db.session.commit()
        flash('La información se ha actualizado correctamente')
        return redirect('/')

    return render_template('editar_cliente.html', cliente=cliente)


if __name__ == '__main__':
    app.run(debug=True)
