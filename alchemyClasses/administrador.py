from alchemyClasses.__init__ import db

class Administrador(db.Model):
    __tablename__ = 'administrador'
    id_admin = db.Column('admin_id',db.Integer, primary_key=True)
    nombre = db.Column('nombre', db.String(50), nullable=False)
    apellidoP = db.Column('apellidoP', db.String(50))
    apellidoM = db.Column('apellidoM', db.String(50))
    email = db.Column('email', db.String(100), nullable=False)
    password = db.Column('password', db.String(50), nullable=False)
    telefono = db.Column('telefono', db.String(20))

    def __init__(self, nombre, apellidoP, apellidoM, edad, email, password, telefono):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.edad = edad
        self.email = email
        self.password = password
        self.telefono = telefono
