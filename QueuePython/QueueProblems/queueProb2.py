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

def placeOrder(orders):
    for order in orders:
        print("Placing order for:", order)
        orderFood.enqueue(order)
        time.sleep(0.5)

def serveOrder():
    time.sleep(1)
    while orderFood.is_empty() == False:
        order = orderFood.dequeue()
        print("Now serving: "+ order)
        time.sleep(2)

print()
if __name__ == '__main__':
    orderList = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=placeOrder, args=(orderList,))
    t2 = threading.Thread(target=serveOrder)
    t1.start()
    t2.start()
