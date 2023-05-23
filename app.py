import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'edgar'
app.config['MYSQL_PASSWORD'] = '123pass'
app.config['MYSQL_DB'] = 'bdd1'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registro_exitoso', methods=['POST'])
def registro_exitoso():
    if request.method == 'POST':
        nombre = request.form['first_name']
        apellidoP = request.form['last_name']
        apellidoM = request.form['2nd name']
        password = request.form['user_password']
        email = request.form['email']
        tel = request.form['contact_no']
        cur = mysql.connection.cursor()
        cur.execute('insert usuario values (0, nombre, apellidoP, apellidoM, 10, email, password , telefono)')
        mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/registro', methods=['GET','POST'])
def registro():
    return render_template('registro.html')

@app.route('/eliminar_cuenta')
def eliminar_cuenta():
    return "xd"

if __name__ == '__main__':
    app.run(debug=True)
