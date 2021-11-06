## Stack
---
### Problems with Array and Linked List
- Dynamic arrays have memory re-allocation problems
- To use linked list you need to traverse the entire list to get to the end
### Operations in Stack (Last in First Out Data Structure)
- Using Last in First Out (LIFO) method: <p align="center"><img src="Images/lifo.png" width="500"></p>
- Keep **pushing** the elements into the data structure
- To go back  you retrieve the element you pushed using **pop**
    - Pop out the last element
### Time Complexity of Stack
- Push/Pop element: O(1)
- Search element by value: O(n)
    - Go through each element and located that particular element
### Use Cases for Stack
- Function calling in any programming language is managed using a stack
    - Function Stack
- Undo functionality (Cmd+Z) in any editor also uses stack to track down last set of operations
### Stack Implementation in Different Languages: <p align="center"><img src="Images/stackLang.png" width="500"></p>
### Problems with using [List as Stack](ListStack.ipynb)
- Problem with list is that it is a dynamic array
- Allocating memory capacity is a problem
    - If list is full of 10 elements and want to add 11th element
    - List will allocated additional capacity elsewhere and copy all the elements there