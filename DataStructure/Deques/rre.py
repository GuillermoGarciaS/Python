from collections import deque

another_deque = deque([1, 2, 3, 4, 5])
another_deque.rotate(len(another_deque))
print(another_deque)

another_deque.reverse()
print(another_deque)

another_deque.extend([6, 7, 8, 9])
print(another_deque)