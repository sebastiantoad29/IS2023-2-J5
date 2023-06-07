from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.usuario import Usuario
from models.model_usuario import get_usuario
from alchemyClasses.usuario import db

actualizar_Cuenta_cliente_bp = Blueprint('actualizar_Cuenta_cliente', __name__, url_prefix='/actualizar_cuenta_cliente')

@actualizar_Cuenta_cliente_bp.route('/cliente/<int:cliente_id>/editar', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    cliente = Usuario.query.get(cliente_id)
    if not cliente:
        return render_template('error_actualizar_cuenta_cliente.html', mensaje='Cliente no encontrado')

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        print(cliente.nombre)
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
