#Importamos el módulo random
import random

#Defino una función que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista
#usando el método random.
def generar_lista():
    lista = []
    for i in range(20):
        lista.append(random.randint(0, 100))
    return lista

#Defino una función que muestre la lista obtenida por pantalla.
def mostrar_lista(lista):
    print(lista)

#Defino una función que ordene los valores de la lista y la muestre por pantalla.
def ordenar_lista(lista):
    lista.sort()
    print(lista)
