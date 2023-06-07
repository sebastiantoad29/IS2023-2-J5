from alchemyClasses.__init__ import db

class Pedido(db.Model):
    pedido_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuario.usuario_id'), nullable=False)
    reporte_generado_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, pedido_id, cliente_id, reporte_generado_id, status):
        self.pedido_id = pedido_id
        self.cliente_id = cliente_id
        self.reporte_generado_id = reporte_generado_id
        self.status = status
