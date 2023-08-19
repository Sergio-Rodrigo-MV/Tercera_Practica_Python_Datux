#  8)
#Programa para poder sumar, restar, multiplicar o dividir dos números 
#ingresado por teclado, hecho por Sergio Mostacero.

#-----------------------------------------------------------------------------------------

import modulo_8_operaciones  

#Imprimo el mensaje de bienvenida y solicito los dos números 'a' y 'b'.
print('¡Bienvenido!')
print('Este programa nos permite sumar, restar, multiplicar y dividir dos numeros enteros.')
a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))

#Defino las cuatro funciones llamadas;
def opcion_1():
   
    sumar = modulo_8_operaciones.suma(a, b)
    print(f'La suma de {a} y {b} es {sumar}')
    
def opcion_2():
  
    rest = modulo_8_operaciones.resta(a, b)
    print(f'La resta de {a} y {b} es {rest}')
   
def opcion_3():
    
    product = modulo_8_operaciones.producto(a, b)
    print(f'La multiplicación de {a} y {b} es {product}')

def opcion_4():
    
    divide = modulo_8_operaciones.division(a, b)
    print(f'La división de {a} y {b} es {divide}')

#Defino el programa principal que tiene un bucle while para poder escoger
#cúal opción desea realizar el usuario.
def main():
    while True :
          opcion = input('Para sumar ingrese 1,Para restar ingrese 2,Para multiplicar ingrese 3,Para dividir ingrese 4, Para salir ingrese 0: ')
         
          
          if opcion == '1':
             opcion_1()
        
          elif opcion == '2':
             opcion_2()
        
          elif opcion == '3':
             opcion_3()
        
          elif opcion == '4':
             opcion_4()
             
          elif opcion == '0':
              print('Gracias por usar este programa.')
              break
             
          else: 
             print("Comando desconocido, vuelve a intentarlo")
          
        
        
if __name__== '__main__':
     main()
     
#Fin del programa
#####################################################################################################################################################
#####################################################################################################################################################
