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
### Stack Implementation in Different Languages: <p align="center"><img src="Images/stackLang.png" width="500"></p>
### Problems with using [List as Stack](ListStack.ipynb)
- Problem with list is that it is a dynamic array
- Allocating memory capacity is a problem
    - If list is full of 10 elements and want to add 11th element
    - List will allocated additional capacity elsewhere and copy all the elements there