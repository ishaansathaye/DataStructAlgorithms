#https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md
#Design a food ordering system where your python program will run two threads:
#   Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#   Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

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
