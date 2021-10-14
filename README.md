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
- Reasoning behind Rules
    - BigO refers to very large value of n
    - If you have a function: time = 5*n^2 + 3*n + 20
        - **When the value of n is very large -> the second and third terms become irrelevant**
- **n refers to iterations**
    - number of computations
- Increasing size input -> time is almost constant
    - time = a
    - Keep fastest growing term
    - Drop constants (a) -> time = **0(1)**
        - Order of 1
- **Everything above also applies to Space Complexity**
- Example of Binary Search
    - Do not want to find number in a list using O(n)
    - If there are billion numbers then program has to do billion iterations 
<p align="center"><img src="Images/binarysearchexample.png" width="450"></p>

- Binary Search (Search for 68 in a sorted list)
    - Find middle number in list and compare to 68 (less than so discard all items to the left)
    - Find middle number and see if less than and then discard left
    - Again divide array by 2 and take middle element is 68
        - Iteration 1 = n/2
        - Iteration 2 = (n/2)/2 = n/2^2
        - Iteration 3 = (n/2^2)/2 = n/2^3
    - Process to 3 iterations, while O(n) would take 7 since 68 in seventh position
    - Iteration k = n/2^k
- **Convert Iteration k = n/2^k to BigO**
    - 1 = n/2^k
        - 1 is worse case scenario
    - n = 2^k
    - log122

