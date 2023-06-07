from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from models.model_login import verificar_credenciales
from alchemyClasses.producto import db

login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_bp.route('/', methods=["GET","POST"])
def indexlgin():
    return render_template('login.html')

@login_bp.route('/logedin', methods=["POST"])
def login():
    email = request.form["inputEmail"]
    password = request.form['inputPassword']
    session['data'] = email

    if verificar_credenciales(email, password, 'administrador'):
        # Autenticación exitosa para el administrador
        session['rol'] = 'administrador'
        return redirect(url_for('login.administrador'))
    elif verificar_credenciales(email, password, 'vendedor'):
        # Autenticación exitosa para el vendedor
        session['rol'] = 'vendedor'
        return redirect(url_for('login.vendedor'))
    elif verificar_credenciales(email, password, 'usuario'):
        # Autenticación exitosa para el usuario
        session['rol'] = 'usuario'
        return redirect(url_for('login.usuario'))
    else:
        # Credenciales inválidas
        return render_template('login.html', error=True)

@login_bp.route('/administrador')
def administrador():
    if session.get('rol') == 'administrador':
        return render_template('administrador.html')
    else:
        return redirect('/')

@login_bp.route('/vendedor')
def vendedor():
    if session.get('rol') == 'vendedor':
        return render_template('vendedor.html')
    else:
        return redirect('/')

@login_bp.route('/usuario')
def usuario():
    if session.get('rol') == 'usuario':
        return render_template('usuario.html')
    else:
        return redirect('/')

# Ruta para cerrar sesión
@login_bp.route('/logout')
def logout():
    session.pop('rol', None)
    return redirect('/')
