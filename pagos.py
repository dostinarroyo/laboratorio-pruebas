class SistemaPagos:

    def calcular_total(self, monto, impuesto):
        return monto + (monto * impuesto)

    def validar_pago(self, monto):
        if monto < 10:
            return False
        if monto > 5000:
            return False
        return True

    def procesar_reembolso(self, dias):
        if dias <= 30:
            return True
        return False