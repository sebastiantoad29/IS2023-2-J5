from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from alchemyClasses.pedido import Pedido
from alchemyClasses.usuario import Usuario
from models.model_pedido import get_pedidos
from models.model_usuario import get_usuario
from alchemyClasses.producto import db
import json


ver_status_bp = Blueprint('ver_status', __name__, url_prefix='/pedidos')

@ver_status_bp.route('/', methods=["GET", "POST"])
def ver_status():
    if 'rol' in session:
        username = session["rol"]
        usuario = get_usuario(session['data'])
        id_usuario = usuario.id_usuario
        pedidos = get_pedidos(id_usuario)
        pedidos_json = [pedido.to_json() for pedido in get_pedidos(id_usuario)]
        print(pedidos_json)
        return render_template('usuario/pedidos/list.html', pedidos=pedidos_json)
    else:
        return render_template('usuario/pedidos/no_session.html')
