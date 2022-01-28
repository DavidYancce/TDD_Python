from constante import Constante


def monto_valido_cuenta(monto_total, tipo_cambio):
    if not isinstance(monto_total, int):
        return False
    return monto_total <= Constante.MONTO_MAXIMO_DOLARES_SCOTIABANK * tipo_cambio

def es_deposito_valido_scotiabank(monto_deposito):
    return monto_deposito % Constante.UNIDAD_DEPOSITO_SOLES_SCOTIABANK == 0

def es_deposito_valido_interbank(monto_deposito):
    return monto_deposito % Constante.UNIDAD_DEPOSITO_DOLARES_INTERBANK == 0
