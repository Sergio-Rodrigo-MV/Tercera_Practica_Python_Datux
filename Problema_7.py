#  7)
#Programa principal para generar una lista de números aleatorios
#y luego ordenarlos de menor a mayor para finalmente mostrarlos por pantalla.
#Hecho por Sergio Mostacero.

#------------------------------------------------------------------------------    
import modulo_7

#Programa Principal.
def main():

# Generar una lista de números aleatorios
 lista = modulo_7.generar_lista()

# Mostrar la lista por pantalla
 modulo_7.mostrar_lista(lista)

# Ordenar la lista y mostrarla por pantalla
 modulo_7.ordenar_lista(lista)
 
if __name__== '__main__':
    main()
    
#Fin del programa principal.
############################################################################
############################################################################