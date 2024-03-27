stack_a = [1, 2, 3, 4]

#Creamos una funcion para agregar el numero 0 a la lista
def push(stack_a, item):
    stack_a.insert(0, item)

#Adjuntamos un objeto al final de la lista
stack_a.append(5)

#Adjuntamos un objeto al inicio de la lista
push(stack_a, 0)

print(stack_a)