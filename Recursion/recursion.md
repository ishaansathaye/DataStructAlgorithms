## Recursion
---
### Theory - How Recursion works
1) Divide big problem into small and simple problem
2) Find a base condition with a simple answer
3) Return base condition answer to solve all sub problems
    - Go up the chain of call stacks
### Example
- **Find a sum of numbers from 1 to n**
    - Find a sum of numbers from 1 to 5
        - 5+(find sum of numbers 1 to 4)
        - 4+(find sum of numbers 1 to 3)
        - 3+(find sum of numbers 1 to 2)
        - 2+(find sum of numbers 1 to 1)
        - *base condition:* find sum of numbers 1 to 1 -> 1
- Go up the call stacks from the base condition