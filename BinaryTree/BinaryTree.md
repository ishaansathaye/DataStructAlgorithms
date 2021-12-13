## Binary Tree
---
### What is a Binary Tree?
- A general tree, but **every node has at most 2 child nodes**
- Binary Search Tree or BST
    - Special case of Binary Tree
    - Elements have an order
    - Elements are always unique
### Searching a BST
- Searching complexity in a list would be order of O(n)
- Searching with through a BST needs to be efficient
    - Searching for element 14: <p align="center"><img src="Images/search14.png" width="500"></p>
    - Do not need to search the right hand side of tree since 14 < 15
### Search Complexity
- Every iteration we reduce search space by 1/2
- n = 8: 8->4->2->1
    - Total number of nodes is 8
    - 3 iterations
    - log base 2 of 8 = 3
- **Search Complexity: O(log n)**
### Inserting an Element in BST
- Evaluate element against each node
- **Inserting Complexity: O(log n)**
### Terminology
- Root Node
- Left Child and Right Child
    - Empty child means null
- Leaf Node - node with no child nodes
- 
### Search Types (Traversal Techniques)
- **Breadth first search**
- **Depth first search**
    - **In Order Traversal**
    - **Pre Order Traversal**
    - **Post Order Traversal**