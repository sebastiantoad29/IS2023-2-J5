from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from alchemyClasses.producto import Producto
from models.model_producto import get_productos
from models.model_producto import get_producto_name
from alchemyClasses.producto import db
import json

hacer_pedido_bp = Blueprint('hacer_pedido', __name__, url_prefix='/pedido')

@ver_productos_bp.route('/', methods=["GET", "POST"])
def ver_lista_productos():
    if request.method == "POST":
        product_data = json.loads(request.form.get('product'))
        nombre_s = product_data['nombre']
        return redirect(url_for('ver_productos.product_detail', nombre=nombre_s))
    else:
        try:
            productos = get_productos()
            products_json = [product.to_json() for product in productos]
            return render_template("producto/ver_productos.html", products=products_json)
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text


@ver_productos_bp.route('/producto/<string:nombre>')
def product_detail(nombre):
    producto = get_producto_name(nombre)
    print(producto.img)
    return render_template("producto/producto_detalle.html", product=producto)
