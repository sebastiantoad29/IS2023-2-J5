from flask import Blueprint, flash, redirect, render_template, request, url_for
from alchemyClasses.vendedor import Vendedor
from alchemyClasses._init_ import db

borrar_bp = Blueprint('borrar', _name_, url_prefix='/borrar')

@borrar_bp.route('/', methods=['GET', 'POST'])
def borrar_vendedor():
    if request.method == 'POST':
        email = request.form['email']

        # Verificar si el vendedor existe en la base de datos
        vendedor = Vendedor.query.filter_by(email=email).first()

        if vendedor:
            # Eliminar al vendedor de la base de datos
            db.session.delete(vendedor)
            db.session.commit()
            flash('El vendedor ha sido eliminado correctamente', 'success')
        else:
            flash('No se encuentra ese correo en el sistema', 'error')

        return redirect(url_for('borrar.borrar_vendedor'))

    return render_template('borrar.html')