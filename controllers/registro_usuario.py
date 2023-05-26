from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.usuario import Usuario
from models.model_usuario import get_usuario
from alchemyClasses.usuario import db

registrar_usuario_bp = Blueprint('registro_usuario', __name__, url_prefix='/registro_usuario')


@registrar_usuario_bp.route('/', methods=["GET", "POST"])
def registro_usuario():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']
        edad = request.form['edad']
        email = request.form['email']
        password = request.form['password']
        tel = request.form['telefono']
        if get_usuario(email) == None:
            nuevo_usuario = Usuario(nombre, apellidoP, apellidoM, edad, email, password, tel)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return render_template("usuario/registro/registro_usuario_exitoso.html")
        else:
            return render_template("usuario/registro/registro_usuario_fallido.html")
    else:
        return render_template('usuario/registro/registro_usuario.html', data="xd")

