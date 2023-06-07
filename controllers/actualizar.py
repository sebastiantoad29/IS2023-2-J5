from flask import Blueprint, render_template, request, Flask
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

actualizar_bp = Blueprint('actualizar', __name__, url_prefix='/actualizar')

@actualizar_bp.route('/vendedor', methods=['GET', 'POST'])
def actualizar_vendedor():
    if request.method == 'POST':
        email = request.form['email']
        vendedor = Vendedor.query.filter_by(email=email).first()

        if vendedor:
            return render_template('admin/actualizar.html', vendedor=vendedor)
        else:
            mensaje = 'No se encontró vendedor con ese correo.'
            return render_template('actualizar.html', mensaje=mensaje)

    return render_template('admin/actualizar.html')

@actualizar_bp.route('/guardar_actualizacion', methods=['POST'])
def guardar_actualizacion():
    email = request.form['email']
    vendedor = Vendedor.query.filter_by(email=email).first()

    if vendedor:
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']
        edad = request.form['edad']
        password=request.form['password']
        telefono = request.form['telefono']
        vendedor = Vendedor(nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM,
                            edad=edad, email=email, password=password, telefono=telefono)
        db.session.add(vendedor)
        db.session.commit()

        mensaje = 'Vendedor actualizado correctamente.'
        return render_template('admin/actualizar.html', mensaje=mensaje)
    else:
        mensaje = 'No se encontró vendedor con ese correo.'
        return render_template('admin/actualizar.html', mensaje=mensaje)
