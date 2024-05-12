class Queue:
    def __init__(self):

        # Creamos 2 stacks, uno para agregar a la cola y otro para borrar de esta
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if len(self.dequeue_stack) == 0:
            while len(self.dequeue_stack) > 0:
                item = self.enqueue_stack.pop()
                self.dequeue_stack.append(item)
        if len(self.dequeue_stack) == 0:
            return None

    def is_empty(self):
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

    def __sizeof__(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

lista = Queue()

# Agregamos datos a la cola
lista.enqueue(5)
lista.enqueue(10)
lista.enqueue(15)
lista.enqueue(20)