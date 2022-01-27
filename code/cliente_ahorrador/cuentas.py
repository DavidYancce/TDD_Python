from pytest import Instance


def monto_valido_cuenta(monto_deposito):
    if(not isinstance(monto_deposito,int)):
        return False
    if(monto_deposito < 1000):
        return True
    return False
