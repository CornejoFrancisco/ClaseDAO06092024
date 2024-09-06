class CuentaBancaria:
    def __init__(self):
        self._saldo = 0
        self.titular = ""
    
    @property
    def saldo(self):
        return self._saldo
    
    
    @saldo.setter
    def saldo(self, valor):
        if (valor > 0):
            self._saldo = valor
    
    
    