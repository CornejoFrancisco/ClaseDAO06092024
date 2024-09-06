class Alumno:
   
   #metodo de inicialización de atributos
   def __init__(self, legajo=0, nombre="", edad=0, nota1=0, nota2=0):
   	  #atributos
       self.legajo = legajo
       self.nombre = nombre
       self.edad = edad
       self.nota1 = nota1
       self.nota2 = nota2
   
   #metodo que retorna la cadena con los valores de los atributos
   def __str__(self):
       return "\nLegajo:"+str(self.legajo)+ " - Nombre:"+str(self.nombre)+\
              "- Edad: " + str(self.edad) + " - Nota1:"+str(self.nota1)+ " - Nota2:"+str(self.nota2)
   
   #metodo para retornar el promedio del alumno
   def promedio(self):
       promedio = (self.nota1 + self.nota2) / 2
       return promedio
   
   def es_mayor_edad(self):
       return self.edad >= 18
   
   
