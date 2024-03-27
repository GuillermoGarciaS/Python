stack_b = [1, 2, 3, 4, 5]

#Imprimimos y eliminamos a la vez el digito al final del stack
print(stack_b.pop())

#Guardamos en una variable el ultimo valor, aunque en el stack este se eliminara
top = stack_b.pop()
print(stack_b)
print(top)