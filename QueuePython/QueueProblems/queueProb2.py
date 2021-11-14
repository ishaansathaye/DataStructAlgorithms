# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md

from collections import deque
import time
import threading

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

orderFood = Queue()
orderList = ['pizza','samosa','pasta','biryani','burger']

def placeOrder():
    pass

def serveOrder():
    pass

t1 = threading.Thread(target=0, args=0)

t1.start()

t1.join()