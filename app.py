from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from alchemyClasses import db
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.usuario import Usuario
from alchemyClasses.administrador import Administrador

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doñaBD.db'
db = SQLAlchemy(app)

# Función para verificar las credenciales en la base de datos
def verificar_credenciales(email, password, tabla):
    if tabla == 'administrador':
        resultado = Administrador.query.filter_by(email=email, password=password).first()
    elif tabla == 'vendedor':
        resultado = Vendedor.query.filter_by(email=email, password=password).first()
    elif tabla == 'usuario':
        resultado = Usuario.query.filter_by(email=email, password=password).first()
    else:
        resultado = None
    return resultado is not None

# Ruta de inicio de sesión
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    if verificar_credenciales(email, password, 'administrador'):
        # Autenticación exitosa para el administrador
        session['rol'] = 'administrador'
        return redirect('/administrador')
    elif verificar_credenciales(email, password, 'vendedor'):
        # Autenticación exitosa para el vendedor
        session['rol'] = 'vendedor'
        return redirect('/vendedor')
    elif verificar_credenciales(email, password, 'usuario'):
        # Autenticación exitosa para el usuario
        session['rol'] = 'usuario'
        return redirect('/usuario')
    else:
        # Credenciales inválidas
        return render_template('login.html', error=True)

# Rutas para el administrador
@app.route('/administrador')
def administrador():
    if session.get('rol') == 'administrador':
        return render_template('administrador.html')
    else:
        return redirect('/')

# Rutas para el vendedor
@app.route('/vendedor')
def vendedor():
    if session.get('rol') == 'vendedor':
        return render_template('vendedor.html')
    else:
        return redirect('/')

# Rutas para el usuario
@app.route('/usuario')
def usuario():
    if session.get('rol') == 'usuario':
        return render_template('usuario.html')
    else:
        return redirect('/')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('rol', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()
