from alchemyClasses.__init__ import db


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column('usuario_id', db.INTEGER, primary_key=True)
    nombre = db.Column('nombre', db.String(50))
    apellidoP = db.Column('apellidoP', db.String(50))
    apellidoM = db.Column('apellidoM', db.String(50))
    edad = db.Column('edad', db.INTEGER, primary_key=True)
    email = db.Column('email', db.String(100))
    password = db.Column('password', db.String(100))
    telefono = db.Column('telefono', db.String(20))

    def __init__(self, nombre, apellidoP, apellidoM,
                 edad, email, password, telefono):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.edad = edad
        self.email = email
        self.password = password
        self.telefono = telefono
