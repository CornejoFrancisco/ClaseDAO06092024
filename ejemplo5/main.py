from persona import Persona
from cuenta import Cuenta

#funcion principal
def main():
    cuenta = None
    #ingresar los datos para crear la cuenta
    print('Ingrese los datos para crear la cuenta: ')
    nombre = input('Ingrese el nombre del titular: ')
    edad = int(input('Ingrese la edad del titular: '))
    dni = input('Ingrese el DNI del titular: ')

    #crea la persona que va a ser el titular de la cuenta
    titular = Persona(nombre, edad, dni)
    #valida que sea mayor de edad
    if titular.esMayorDeEdad():
        monto = float(input('Ingrese el monto inicial de la cuenta: '))
        #se crea la cuenta
        cuenta = Cuenta(titular, monto)
        print('Se creo la cuenta con un saldo inicial de: $', cuenta.mostrar_saldo())
    else:
        print('No se puede crear la cuenta ya que la persona es menor de edad')

    #verificar que la cuenta exista
    if cuenta != None:
        #depositar
        monto = float(input('Ingrese el monto a depositar: '))
        if cuenta.depositar(monto):
            print('El saldo actual de la cuenta es: $', cuenta.mostrar_saldo())
        #extraer
        monto = float(input('Ingrese el monto a extraer: '))
        if cuenta.extraer(monto):
            print('Se pudo extraer $', monto, ' y el saldo actual de la cuenta queda en: $', cuenta.mostrar_saldo())
        else:
            print('Fondos insuficientes, NO se pudo extraer $', monto, ' tiene un saldo actual en la cuenta de: ', cuenta.mostrar_saldo())
    else:
        print('La cuenta no se pudo crear')

#invocacion
main()