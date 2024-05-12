class Queue:
    def __init__(self):
        """
Inicializa una nueva cola.
"""
        self.items = []  # Lista para almacenar los elementos

    def enqueue(self, data):
        """
Agrega un elemento al final de la cola.

Args:
    data: Los datos a agregar a la cola.
"""
        self.items.append(data)

    def dequeue(self):
        """
Elimina y devuelve el elemento al frente de la cola.

Returns:
    El elemento eliminado del frente de la cola, o None si la cola está vacía.
"""
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def front(self):
        """
Devuelve el elemento al frente de la cola sin eliminarlo.

Returns:
    El elemento al frente de la cola, o None si la cola está vacía.
"""
        if len(self.items) == 0:
            return None
        return self.items[0]

    def rear(self):
        """
Devuelve el elemento al final de la cola sin eliminarlo.

Returns:
    El elemento al final de la cola, o None si la cola está vacía.
"""
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        """
Devuelve el número de elementos en la cola.

Returns:
    El número de elementos en la cola.
"""
        return len(self.items)

    def is_empty(self):
        """
Verifica si la cola está vacía.

Returns:
    True si la cola está vacía, False en caso contrario.
"""
        return len(self.items) == 0


# Define una función que simula el proceso de impresión usando una cola
def print_documents(documents):
    """
Simula el proceso de impresión usando una cola.
Solicita documentos al usuario y los imprime en el formato especificado.

Returns:
    Una lista de cadenas que indican el estado de impresión de cada documento.
"""
    doc_details = []
    queue = Queue()
    for document in documents:
        queue.enqueue(document)
    time = 0
    while not queue.is_empty():
        document = queue.dequeue()
        if document is not None:  # Verifica si document no es None
            name = document[0]
            pages = document[1]
            print_time = pages / 2
            time += print_time
            doc_details.append(f"Document {name} printed in {print_time} minutes.")

    return doc_details
