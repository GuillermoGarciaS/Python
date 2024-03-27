# Python code below
# Define a node class for the linked list

string = input("Ingresa tu polindromo: ")

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Define a stack class using a linked list
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

# Define a function that checks if a string is a palindrome using a stack
def isPalindrome(string):
  string = string.lower()
  string = string.replace(" ", "")
  string = string.replace("á", "a")
  string = string.replace("í", "i")
  string = string.replace("é", "e")
  string = string.replace("ó", "o")
  string = string.replace("ú", "u")
  
  a = 0
  b = len(string) - 1

  for i in range (0, len(string)):
        if string[a] == string[b]:
            a += 1
            b -= 1
        else:
            return False
        return True