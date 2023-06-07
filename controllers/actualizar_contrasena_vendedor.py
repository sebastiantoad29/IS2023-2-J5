from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.usuario import db

actualizar_contrasena_vendedor_bp = Blueprint('actualizar_contrasena_vendedor', __name__, url_prefix='/actualizar_contrasenia_vendedor')



@actualizar_contrasena_vendedor_bp.route('/vendedor/<int:vendedor_id>/actualizar-contrasena', methods=['GET', 'POST'])
def actualizar_contrasena(vendedor_id):
    vendedor = Vendedor.query.get(vendedor_id)
    if not vendedor:
        return render_template('error_contrasena.html', mensaje='Vendedor no encontrado')

    if request.method == 'POST':
        nueva_contrasena = request.form['contrasena']
        confirmar_contrasena = request.form['confirmar_contrasena']

        if nueva_contrasena != confirmar_contrasena:
            return render_template('error_contrasena.html', mensaje='Las contraseñas no coinciden')

        vendedor.password = nueva_contrasena
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('actualizar_contrasena.html', vendedor=vendedor)
