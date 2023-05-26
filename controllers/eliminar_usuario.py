from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.usuario import Usuario
from models.model_usuario import get_usuario
from alchemyClasses.usuario import db

eliminar_usuario_bp = Blueprint('eliminar_usuario', __name__, url_prefix='/eliminar_usuario')


@eliminar_usuario_bp.route('/', methods=["GET", "POST"])
def eliminar_usuario():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = get_usuario(email)
        if user != None and user.password == password:
            Usuario.query.filter_by(email=email).delete()
            db.session.commit()
            print("Se eliminó el usuario de la base de datos.")
            return render_template("usuario/eliminarCuenta/baja_usuario_exitosa.html")
        else:
            print("No existe el producto.")
            return render_template("usuario/eliminarCuenta/baja_usuario_fallida.html")
    else:
        return render_template('usuario/eliminarCuenta/baja_usuario.html')

