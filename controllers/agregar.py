from flask import Blueprint, render_template, request
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

agregar_bp = Blueprint('agregar', __name__, url_prefix='/agregar')

@agregar_bp.route('/', methods=['GET', 'POST'])
def agregar_vendedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']
        edad = int(request.form['edad'])
        email = request.form['email']
        password = request.form['password']
        telefono = int(request.form['telefono'])

        vendedor = Vendedor(nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM,
                            edad=edad, email=email, password=password, telefono=telefono)
        db.session.add(vendedor)
        db.session.commit()

        return 'Vendedor agregado correctamente'
    else:
        return render_template('admin/agregar.html')
