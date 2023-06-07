from alchemyClasses.pedido import Pedido

def get_pedidos(id_usuario):
    pedidos = Pedido.query.filter(Pedido.cliente == id_usuario).all()
    return pedidos
