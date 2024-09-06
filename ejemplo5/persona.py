class Persona:
   #utiliza argumentos por defecto
   def __init__(self,nombre="",edad=0,dni=""):

       self.nombre=nombre
       self.edad=edad
       self.dni=dni

   def __str__(self):

       return "Nombre:"+self.nombre+" - Edad:"+str(self.edad)+" - DNI:"+self.dni

   def esMayorDeEdad(self):
       return self.edad >= 18

