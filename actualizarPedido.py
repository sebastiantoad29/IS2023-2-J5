from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from alchemyClasses.pedido import Pedido


app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doñaBD.db'
db = SQLAlchemy(app)

@app.route('/')
def mostrar_status_pedido():
    pedidos = Pedido.query.all()
    return render_template('status.html', pedidos=pedidos)
    

@app.route('/update_status', methods=['POST'])
def actualizar_status():
    pedido_id = request.form['pedido_id']
    new_status = request.form['new_status']
    
    pedido = Pedido.query.get(pedido_id)
    pedido.status = new_status
    db.session.commit()
    
    pedidos = Pedido.query.all()
    return render_template('status.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run()