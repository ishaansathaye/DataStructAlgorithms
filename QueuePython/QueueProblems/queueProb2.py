# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md
#Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. 

from collections import deque

class Queue:
    
    def __init__(self) -> None:
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

def makeBinaryNum(n):
    numQueue = Queue()
    numQueue.enqueue('1')

    for i in range(n):
        front = numQueue.front()
        print(front)
        numQueue.enqueue(front+'0')
        numQueue.enqueue(front+'1')
        numQueue.dequeue()

print()
makeBinaryNum(10)
print()