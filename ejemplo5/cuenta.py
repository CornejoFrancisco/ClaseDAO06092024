

class Cuenta:
    def __init__(self, persona, saldo =0):
        self.persona = persona
        self.saldo = saldo
    
    def __str__(self):
        return "Cuenta\n" + "Titular " + str(self.persona) + " - Saldo: " + str(self.saldo)
    
    def mostrar_saldo(self):
        return self.saldo
    
    def depositar(self, monto):
        operacion = False
        if(monto >= 0):
            self.saldo = self.saldo + monto
            operacion = True
        return operacion
    
    def extraer(self, monto):
        operacion = False
        if self.mostrar_saldo() >= monto:
            self.saldo = self.saldo - monto
            operacion = True
        return operacion