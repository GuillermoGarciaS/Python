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
    data = self.head.data
    self.head = self.head.next
    return data

  def peek(self):
    if self.head is None:
        return None
    return self.head.data

  def isEmpty(self):
    return self.head == None

# Define a function that checks if a string is a palindrome using a stack
def isPalindrome(string):
  string = string.lower()
  string = "".join(c for c in string if c.isalnum())
  stack = Stack()
  for c in string:
      if c != stack.pop():
        return False
  return True