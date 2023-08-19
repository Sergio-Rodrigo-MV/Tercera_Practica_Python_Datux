# Importar el módulo random
import random

# Definir una función que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista
def generar_lista():
    lista = []
    for i in range(20):
        lista.append(random.randint(0, 100))
    return lista

# Definir una función que muestre la lista obtenida por pantalla
def mostrar_lista(lista):
    print(lista)

# Definir una función que ordene los valores de la lista y la muestre por pantalla
def ordenar_lista(lista):
    lista.sort()
    print(lista)