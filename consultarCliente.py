from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from alchemyClasses.usuario import Usuario

app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doñaBD.db'
db = SQLAlchemy(app)

@app.route('/')
def mostrar_clientes():
    clientes = db.session.query(Usuario).all()
    return render_template('consultarClientes.html', clientes=clientes)

if __name__ == '__main__':
    app.run()