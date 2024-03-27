stack_c = [1, 2, 3, 4]

#Al usar el '-1' para buscar un valor en el stack, automaticamente nos dara el ultimo valor
print(stack_c[-1])
print(stack_c)

#Creamos una pila vacia para realizar una prueba
stack_d = []

#Dado que intentar buscar un valor dentro de una pila vacia nos dara un error, crearemos un try except
#Esto con el fin de evitar errores y poder generar casos de exepcion
try:
    print(stack_d[-1])
except IndexError:
    print("Tu pila esta vacia")