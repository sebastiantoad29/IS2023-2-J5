from alchemyClasses.producto import Producto

def get_productos():
    products = Producto.query.all()
    return products


def get_producto_name(nombre):
    product = Producto.query.filter(Producto.nombre == nombre).first()
    return product
