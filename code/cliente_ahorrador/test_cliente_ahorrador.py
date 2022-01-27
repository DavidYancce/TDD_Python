from cuentas import monto_valido_cuenta

def test_cuenta_valida_scotiabank():
    assert not monto_valido_cuenta(1500), "No debe de superar los 1000 dolares"

def test_nulidad_cuenta_scotiabank():
    assert not monto_valido_cuenta(None), "No debe de haber un monto"

def test_string_cuenta_scotiabank():
    assert not monto_valido_cuenta("adios mundo"), "No debe de ser un string"
