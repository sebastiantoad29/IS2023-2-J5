from flask import Blueprint, render_template, request
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

ver_bp = Blueprint('ver', _name_, url_prefix='/ver')

@ver_bp.route('/', methods=['GET', 'POST'])
def ver_vendedor():
    if request.method == 'POST':
        email = request.form['email']
        vendedor = Vendedor.query.filter_by(email=email).first()