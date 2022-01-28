from pytest import Instance


def monto_valido_cuenta(monto_total, tipo_cambio):
    if not isinstance(monto_total, int):
        return False
    return monto_total < 1000 * tipo_cambio

def es_deposito_valido_scotiabank(monto_deposito):
    return monto_deposito % 50 == 0
    
