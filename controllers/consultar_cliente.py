from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.usuario import Usuario
from models.model_usuario import get_usuario
from alchemyClasses.usuario import db

consultar_clientes_bp = Blueprint('consultar_cliente', __name__, url_prefix='/consulta_clientes')


@consultar_clientes_bp.route('/')
def mostrar_clientes():
    clientes = db.session.query(Usuario).all()
    return render_template('consultarClientes.html', clientes=clientes)
