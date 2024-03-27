class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.isEmpty():
            return None
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data
    
    def isEmpty(self):
        return self.head is None
    
stack = Stack()

numeros = []

for i in range(1, 11):
    numeros.append(i)
    print(numeros[-1])

for numero in numeros[:]:
    numero_poppeado = numeros.pop()
    print(numero_poppeado)