class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        # En caso de que la lista no tenga datos
        if len(self.queue) == 0:
            # Retornamos un None
            return None
        else:
            # Le atribuimos el 1er valor insertado a la variable item
            item = self.queue[0]
            # Ahora acualizamos la cola removiendo el 1er dato
            self.queue = self.queue[1:]
            return item

    # Comprobamos que la lista este vacia o no
    def is_empty(self):
        return len(self.queue) == 0

    # Obtenemos el tamaño de la lista
    def size(self):
        return len(self.queue)

#Creamos

lista = Queue()

# Agregamos datos a la cola
lista.enqueue(5)
lista.enqueue(10)
lista.enqueue(15)
lista.enqueue(20)

# Imprimimos la longitud de la cola
print("La lista tiene una longitud total de: ",lista.size(), "\n")
# Imprimimos los valores de la lista

counter = 1
for i in lista.queue:
    print("El item con el valor ", counter, " es: ", i)
    counter += 1

# Eliminamos todos los valores mientras los vamos imprimiendo

counterDos = 1
for i in lista.queue:
    lista.dequeue()

# Corroboramos que los datos han sido eliminados
print("\nLa longitud actual de la lista es de ",lista.size())