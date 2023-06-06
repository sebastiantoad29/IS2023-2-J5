from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

Actualizar_contrasenia_vendedor_bp = Blueprint('Actualizar_contrasenia_vendedor', __name__, url_prefix='/Actualizar_contrasenia_vendedor')


class Vendedor(db.Model):
    id_vendedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidoP = db.Column(db.String(50), nullable=False)
    apellidoM = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(45), nullable=False)

@app.route('/vendedor/<int:vendedor_id>/actualizar-contrasena', methods=['GET', 'POST'])
def actualizar_contrasena(vendedor_id):
    vendedor = Vendedor.query.get(vendedor_id)
    if not vendedor:
        return render_template('error_contrasena.html', mensaje='Vendedor no encontrado')

    if request.method == 'POST':
        nueva_contrasena = request.form['contrasena']
        confirmar_contrasena = request.form['confirmar_contrasena']

        if nueva_contrasena != confirmar_contrasena:
            return render_template('error_contrasena.html', mensaje='Las contraseñas no coinciden')

        vendedor.contraseña = nueva_contrasena
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('actualizar_contrasena.html', vendedor=vendedor)


if __name__ == '__main__':
    app.run(debug=True)
