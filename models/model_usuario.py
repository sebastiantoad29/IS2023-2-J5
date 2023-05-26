from alchemyClasses.usuario import Usuario


def get_usuario(email):
    ans = Usuario.query.filter(Usuario.email == email).first()
    return ans
