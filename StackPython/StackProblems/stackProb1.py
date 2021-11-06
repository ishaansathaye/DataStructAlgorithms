from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(value):
    s = Stack()
    convertList = list(value)
    for item in convertList:
        s.push(item)
    temp = ''
    while s.size() != 0:
        temp += s.pop()
    return temp

print()
print(reverse_string("We will conquere COVID-19"))
print()