from collections import deque

my_deque = deque()
my_deque.append(1)
my_deque.appendleft(2)
my_deque.appendleft(3)
print(my_deque)

my_deque.pop()
my_deque.popleft()

print(my_deque)