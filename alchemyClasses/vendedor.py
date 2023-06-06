from alchemyClasses.__init__ import db
from sqlalchemy import text

class Vendedor(db.Model):
    _tablename_ = 'vendedor'

    vendedor_id = db.Column('vendedor_id',  db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    apellidoP = db.Column('apellidoP', db.String(45))
    apellidoM = db.Column('apellidoM', db.String(45))
    edad = db.Column('edad', db.Integer)
    email = db.Column('email', db.String(45))
    password = db.Column('password', db.String(45))
    telefono = db.Column('telefono', db.Integer)

    def _init_(self, vendedor_id, nombre, apellidoP, apellidoM, edad, email, password, telefono):
        self.vendedor_id = vendedor_id
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.edad = edad
        self.email = email
        self.password = password
        self.telefono = telefono