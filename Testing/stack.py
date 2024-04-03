class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped = self.top
        self.top = self.top.next
        return popped.data
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data
            
    def isEmpty(self):
        return self.top is None
    
def isPalindrome(string):

    stack = Stack()
    string = ''.join(char.lower() for char in string if char.isalnum())

    for char in string:
        stack.push(char)

    reversed_string = ''
    while not stack.isEmpty():
        reversed_string += stack.pop()
    
    return string == reversed_string
    
input_strings = []
num_inputs = int(input())

for i in range(num_inputs):
    input_string = input(f"enter string {i+1}:")
    input_strings.append(input_string)

for input_string in input_strings:
    palindrome_status = isPalindrome(input_string)
    print(f"{input_string}")
    print(palindrome_status)