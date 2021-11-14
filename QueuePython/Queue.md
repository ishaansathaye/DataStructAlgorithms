## Queue
---
### Example: Stock Price Exchange Without Queue
- Issue #1: What if HTTP server is down -> Loss of messages
- Issue #2: Managing multiple consumers becomes problematic
- **Queue establishes loose coupling**
    - Also called Producer-Consumer problem
        - One entity is producing information and another entity is consuming the information in away that they are not tightly coupled
### FIFO
- First in First Out
    - Example: Person standing in line for movie tickets
### Stack Implementation in Different Languages: <p align="center"><img src="Images/diffQueueLang.png" width="500"></p>
### Problems with using List as Queue
- Allocating new memory for new elements that exceed the current capacity
- Not recommended (can use ```deque``` in Python or implement queue using linked list)
### Big O Time Complexity
- Access: O(n)
- Search: O(n)
- Insertion: O(1)
- Deletion: O(1)