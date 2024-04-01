# Python code below
# Define a node class for the linked list

string = input()

class Node:
    def __init__(self, data):
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
    
# Define a function that checks if a string is a palindrome using a stack
def isPalindrome(string):
  string_normalizada = ''.join(char.lower() for char in string if char.isalnum())

  stack = Stack()

  if not string_normalizada:
      return False


  mitad = len(string_normalizada) // 2
  for char in string_normalizada[:mitad]:
     stack.push(char)

  if len(string_normalizada) % 2 != 0:
     mitad += 1
     

  for char in string_normalizada[mitad:]:
    if char != stack.pop():
        return False
    

  return True

if isPalindrome(string):
   print(True)
else: print(False)