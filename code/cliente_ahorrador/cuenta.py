from constante import Constante
class Cuenta:
    def __init__(self, codigo=None, entidad_bancaria=None, saldo=0, divisa=None):
        self.codigo = codigo
        self.entidad_bancaria = entidad_bancaria
        self.saldo = saldo
        self.divisa = divisa

    def es_deposito_valido(self, monto_deposito):
        if self.entidad_bancaria == 'scotiabank':
            return monto_deposito % Constante.UNIDAD_DEPOSITO_SOLES_SCOTIABANK == 0
        return monto_deposito % Constante.UNIDAD_DEPOSITO_DOLARES_INTERBANK == 0
    
    def es_valida(self, tipo_cambio):
        if not isinstance(self.saldo, int):
            return False
        return self.saldo <= Constante.MONTO_MAXIMO_DOLARES_SCOTIABANK * tipo_cambio
