from alchemyClasses.__init__ import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    usuario_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidoP = db.Column(db.String(50), nullable=False)
    apellidoM = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20))

    def __init__(self, nombre, apellidoP, apellidoM, edad, email, password, telefono):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.edad = edad
        self.email = email
        self.password = password
        self.telefono = telefono