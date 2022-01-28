from cuenta import Cuenta
from cuentas import (
    monto_valido_cuenta,
    es_deposito_valido_scotiabank,
    es_deposito_valido_interbank
)

def validar_monto_menor_1000_dolares_scotiabank():
    cuenta_scotiabank = Cuenta('1001', 'scotiabank', 1500, 'PEN')
    assert cuenta_scotiabank.es_valida(4), "No debe de superar los 1000 dolares"

def validar_monto_mayor_1000_dolares_scotiabank():
    assert not monto_valido_cuenta(4100, 4), "El monto esta superando los 1000 dolares"

def validar_nulidad_cuenta_scotiabank():
    assert not monto_valido_cuenta(None, 4), "Debe de haber un monto"

def validar_string_cuenta_scotiabank():
    assert not monto_valido_cuenta("adios mundo", 4), "No debe de ser un string"

def test_cuenta_valida_scotiabank():
    validar_monto_menor_1000_dolares_scotiabank()
    validar_monto_mayor_1000_dolares_scotiabank()
    validar_nulidad_cuenta_scotiabank()
    validar_string_cuenta_scotiabank()



def test_deposito_no_valido_scotiabank():
    assert not es_deposito_valido_scotiabank(132), "Debe de ser multiplo de 50"

def test_deposito_no_valido_interbank():
    assert not es_deposito_valido_interbank(225), "El deposito debe de ser en miles de dolares"
