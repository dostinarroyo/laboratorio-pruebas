from pagos import SistemaPagos

def test_calcular_total():
    sistema = SistemaPagos()

    resultado = sistema.calcular_total(100, 0.18)

    assert resultado == 118.0


def test_pago_valido():
    sistema = SistemaPagos()

    resultado = sistema.validar_pago(100)

    assert resultado is True


def test_pago_muy_bajo():
    sistema = SistemaPagos()

    resultado = sistema.validar_pago(5)

    assert resultado is False


def test_pago_muy_alto():
    sistema = SistemaPagos()

    resultado = sistema.validar_pago(6000)

    assert resultado is False


def test_reembolso_valido():
    sistema = SistemaPagos()

    resultado = sistema.procesar_reembolso(15)

    assert resultado is True