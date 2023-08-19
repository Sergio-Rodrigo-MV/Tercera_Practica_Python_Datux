# Este es el módulo operaciones.py

def suma(a, b):
    # Esta función devuelve la suma de dos números
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no válido")

def resta(a, b):
    # Esta función devuelve la resta de dos números
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no válido")

def producto(a, b):
    # Esta función devuelve el producto de dos números
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no válido")

def division(a, b):
    # Esta función devuelve la división de dos números
    try:
        return a / b
    except TypeError:
        print("Error: Tipo de dato no válido")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")