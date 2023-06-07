from alchemyClasses.vendedor import Vendedor


def get_vendedor(email):
    ans = Vendedor.query.filter(Vendedor.email == email).first()
    return ans
