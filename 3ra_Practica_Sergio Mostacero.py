#Tercera Práctica de Python.

#  1)
#Programa para solicitar al usuario ingresar dos numeros enteros
#y le devuelva una fracción de estos, hecho por Sergio Mostacero.

#-----------------------------------------------------------------

#Definio la funcion 'fraccion' y pido que se ingrese los valores de 'x' e 'y' por
#teclado.
def fraccion():
    while True:
        
        #Uso el bloque try - except para evitar los errores por 'ZeroDivisionError' y
        #ValueError. 
        try:
            x = int(input('Ingrese el primer número entero: '))
            y = int(input('Ingrese el segundo número entero: '))
            
            fraction_num = (x/y)*100
            
            if fraction_num < 1:
                
                print('E')
                  
            elif fraction_num > 99:
                print('F')
                
            else:
                print(f'El porcentaje es {fraction_num} %')    
            break
        
        except ZeroDivisionError :
            print('Ha ocurrido un error: ¡La división por 0 no esta definida!')
            
        except ValueError :
            print('Ha ocurrido un error: ¡Ingrese numeros enteros!')   
        
            return fraccion()

#Llamo a la función.       
fraccion()

#Fin del programa.
#######################################################################################
####################################################################################### 

#  2)
#Programa para almacenar las notas de los alumnos en una lista y
# despues pasar cada elemento de la lista a numeros enteros, hecho por 
#Sergio Mostacero.

#---------------------------------------------------------------------

#Solicito al usuario una lista de calificaciones separadas por comas.
calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")

# Creamos una lista vacía para almacenar las calificaciones convertidas a enteros.
calificaciones_int = []

#Utilizo el método 'split' para dividir la cadena en calificaciones individuales. 
calificaciones_split = calificaciones.split(",")

# Recorremos la lista de calificaciones individuales con un ciclo for, utilizando los 
#bolques try - except para evitar los errores. Tambíen convertimos a entero cada valor de
#la variable 'calificacion' para despues agregarla a lista vacía.

for calificacion in calificaciones_split:
   
    try:
        calificacion_int = int(calificacion)
        calificaciones_int.append(calificacion_int)
    
    except ValueError:
        print(f"La calificación {calificacion} no es válida y no se pudo convertir a entero")

#Mostramos la lista de calificaciones enteras.
print(f"La lista de calificaciones enteras es: {calificaciones_int}")

#Fin del programa.
###############################################################################################
###############################################################################################

#  3)
#Problema para calcular el área de un círculo conociendo su radio definiendo 
#una clase llamada 'círculo' y un atributo llamado 'radio', hecho por Sergio Mostacero.

#-------------------------------------------------------------------------------------

#Importo la librería 'math' y defino la clase 'circulo', mediante metodo __init__ con el 
#atributo 'radio'.
import math 

class circulo:
      def __init__(self,radio):
            self.radio = radio
       
      def area_circulo(self):
            return math.pi * (self.radio)**2 

#Pruebo la clase 'circulo' definiendo un objeto 'area_s'.         
area_s = circulo(2)       
       
print(f'El área del círculo es {area_s.area_circulo()} centimetros cuadrados. ')

#Fin del programa.
############################################################################################
############################################################################################ 

#  4)
#Problema para calcular el área de un rectangulo conociendo la medida del ancho
# y el largo definiendo una clase llamada 'rectangulo', hecho por Sergio Mostacero.

#----------------------------------------------------------------------------------

class rectangulo:
      def __init__(self,largo,ancho):
          self.largo = largo
          self.ancho = ancho
      
      def area_rectangulo(self): 
          return self.largo * self.ancho

#Pruebo la clase 'rectangulo' definiendo un objeto 'area_1'.    
area_1 =  rectangulo(12,2)
print(f'El área del rectangulo es {area_1.area_rectangulo()} centimetros cuadrados.')

#Fin del programa.
######################################################################################
######################################################################################

#  5)
#Programa para crear una clase llamada Alumno e iniciarla con el nombre 
# y número de registro, hecho por Sergio Mostacero.

#----------------------------------------------------------------------

#Defino la clase 'Alumno' con los atributos 'nombre' y 'numero_registro.'
class alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
    
    #Defino la función display para mostrar la información del alumno.
    def display(self):
      
       print(f'El alumno registrado es {self.nombre} con número de registro {self.numero_registro}' ) 
    
    #Defino la función setage para mostrar la edad del alumno.   
    def setage(self,edad):
        self.edad = edad
        print(f'Su edad es {edad}')
    
    #Defino la función setnota para mostrar la nota del alumno.
    def setnota(self, nota):
        self.nota = nota
        print(f'Su nota es {nota}')

#Creamos el objeto 'alumno_1' para pobrar la clase.
alumno_1 = alumno('Sergio',920513921)  
alumno_1.display()
alumno_1.setage(24)
alumno_1.setnota(20)

#Fin del programa.
##################################################################################
##################################################################################

#  6)
#Problema para saber en el cuadrante se encuentra un punto sabiendo sus 
#coordenadas x e y, hecho por Sergio Mostacero.

#-----------------------------------------------------------------------
#Creo la clase 'Punto'
class Punto:
    #Iniciamos la clase con los atributos 'x=0' e 'y=0'
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    #Sobreescribir el método string para imprimir el punto en formato (x,y).
    def __str__(self):
        return f"({self.x},{self.y})"
    
    #Definir un método que indique a qué cuadrante pertenece el punto.
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return f"El punto {self.x},{self.y} pertenece al primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto {self.x},{self.y} pertenece al segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto {self.x},{self.y} pertenece al tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto {self.x},{self.y} pertenece al cuarto cuadrante."
        elif self.x == 0 and self.y != 0:
            return "El punto esta sobre el eje Y."
        elif self.x != 0 and self.y == 0:
            return "El punto esta sobre el eje X."
        else:
            return "El punto es el origen."
    
    # Definir un método que calcule el vector resultante entre dos puntos
    def vector(self, otro):
        return Punto(otro.x - self.x, otro.y - self.y)
    
punto_1 = Punto(2,4)
punto_2 = Punto(5,7)
print(punto_1.cuadrante())
print(punto_2.cuadrante())

# Llamar al método vector para obtener el vector resultante entre los dos puntos
print('El vector resultante es: ', punto_1.vector(punto_2))

#Fin del programa
##################################################################################
##################################################################################

