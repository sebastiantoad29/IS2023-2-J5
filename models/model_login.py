from alchemyClasses.vendedor import Vendedor
from alchemyClasses.usuario import Usuario
from alchemyClasses.administrador import Administrador

def verificar_credenciales(email, password, tabla):
    if tabla == 'administrador':
        resultado = Administrador.query.filter(Administrador.email==email, Administrador.password==password).first()
    elif tabla == 'vendedor':
        resultado = Vendedor.query.filter(Vendedor.email==email, Vendedor.password==password).first()
    elif tabla == 'usuario':
        resultado = Usuario.query.filter(Usuario.email==email, Usuario.password==password).first()
    else:
        resultado = None
    return resultado is not None
