from alchemyClasses.__init__ import db


class Producto(db.Model):
    __tablename__ = 'producto'
    id_producto = db.Column('id_producto', db.INTEGER, primary_key=True)
    nombre = db.Column('nombre', db.String(50))
    precio = db.Column('precio', db.INTEGER)
    descripcion = db.Column('descripcion', db.String(500))
    img = db.Column('img', db.String(255))
    inventario = db.Column('inventario', db.INTEGER)

    def to_json(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion,
            'img': self.img
        }


    def __init__(self, nombre, precio, img):
        self.nombre = nombre
        self.edad = edad
        self.img = img
