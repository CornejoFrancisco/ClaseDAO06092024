from faker import Faker
from alumno import Alumno


def cargar_lista(n):
    lista = []
    faker = Faker()
    for i in range(n):
        leg = faker.pyint(1, 9999)
        nom = faker.name()
        edad = faker.pyint(0, 100)
        nota1 = faker.pyint(1, 10)
        nota2 = faker.pyint(1, 10)
        alum = Alumno(leg, nom, edad, nota1, nota2)
        lista.append(alum)
    return lista


def str_lista(lista):
    listado = '\nLos datos de los alumnos son: \n'
    listado += '\n' + ('-' * 50)
    
    for alu in lista:
        listado += str(alu) + '\n'
    return listado


def es_mayor_edad(lista):
    for i in range(len(lista)):
        if lista[i].es_mayor_edad():
            print(lista[i].nombre, 'es mayor de edad')
        if not lista[i].es_mayor_edad():
            print(lista[i].nombre, 'es menor de edad')


def promedio_edad(lista):
    suma = 0
    n = len(lista)
    for i in range(n):
        suma += lista[i].edad
    if n > 0:
        promedio = suma / n
    else:
        promedio = 0
    return promedio


def get_promedio(lista):
    suma = 0  # Inicializamos la variable suma
    n = len(lista)
    for i in range(n):
        suma += lista[i].promedio()
    if n > 0:
        promedio = suma / n
    else:
        promedio = 0  # Si no hay alumnos, el promedio es 0

    return promedio 


def main():
    # Pide la cantidad de alumnos a cargar
    n = int(input('\nIngrese la cantidad de alumnos a cargar: '))

    # Genera y carga la lista de alumnos
    lista = cargar_lista(n)

    # Invoca a las funciones y muestra los resultados
    print('Los elementos de la lista son: ', str_lista(lista))
    print('El promedio general de los alumnos es : ', get_promedio(lista))
    print('El promedio de edad de los alumnos es: ', promedio_edad(lista))
    es_mayor_edad(lista)

main()
