from alchemyClasses.__init__ import db


class Pedido(db.Model):
    __tablename__ = 'pedido'
    pedido_id = db.Column('pedido_id', db.INTEGER, primary_key=True)
    cliente = db.Column('cliente_id', db.String(50))
    reporte = db.Column('reporte_generado_id', db.String(50))
    status = db.Column('status', db.String(255))

    def to_json(self):
        return {
            'pedido': self.pedido_id,
            'cliente': self.cliente,
            'reporte': self.reporte,
            'status': self.status
        }
