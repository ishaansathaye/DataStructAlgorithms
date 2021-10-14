# Data Structures and Algorithms in Python

## Why need Data Structures?
- Raw building blocks
    - array, linked lists, trees...
- Definition: Building blocks or raw materials for any software programs
- **Use right data structure for a problem**
- Data Structures - containers storing data in a specific memory layout
- **Array vs Dictionary (Hash Map) Memory Visual:** <p align="center"><img src="Images/memory_visual.png" width="450"></p>
    - Dictionary uses Hash Map
        - There is a key that gives and address of a bucket, which gives access to an element
- **Data Structures in different languages:** <p align="center"><img src="Images/data_languages.png" width="450"></p>
---
## Measuring Time Complexity
- **Big O notation** - used to measure how running time or space requirements for your program grow as input size grows
    - Used for all programming languages
- Notation Rules:
    1. Keep fastest growing term (time = a*n)
    2. Drop constants (time = 0(n))
- n refers to iterations
    - number of computations
- increasing size input -> time is almost constant
    - time = a
    - Keep fastest growing term
    - Drop constants (a) -> time = **0(1)**
        - Order of 1