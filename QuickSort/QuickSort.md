## Quick Sort
---
### Quick Sort Technique
1) Take a pivot (a number), put pivot in the right position, where left side less than pivot and right side greater than pivot: <p align="center"><img src="Images/pivot.png" width="240"></p>
2) Pick the pivot of one side and repeat step above with that side: <p align="center"><img src="Images/pivot2.png" width="240"></p>
3) Find the pivot of the final side and repeat first step: <p align="center"><img src="Images/pivot3.png" width="240"></p>
- *Partitioning* - process of putting a pivot in its right position
### **Two Types of Partition Schemes: Hoare Partition and Lomuto Partition**
- <mark>Hoare Partition:</mark>
    - Partitioning:
        1) Pivot is the leftmost element
        2) Have a Start and End Pointer: <p align="left"><img src="Images/hoare.png" width="240"></p>
        3) Focus on start pointer -> *move start pointer until found element greater than pivot*
        4) Then focus on end pointer -> *reduce end pointer until element less than pivot*
        5) Swap start and end elements: <p align="left"><img src="Images/swap.png" width="240"></p>
        6) Repeat process from step 2 of choosing start and end pointer
        7) *Stop the process whenever end pointer crosses start pointer*: <p align="left"><img src="Images/cross.png" width="240"></p>
            - If pointers cross -> *swap end and pivot*
    - Repeat above process for left and right side
- **Lomuto Partition**
    - Partitioning:
### Searching a BST
- Searching complexity in a list would be order of O(n)
- Searching with through a BST needs to be efficient
    - Searching for element 14: <p align="center"><img src="Images/search14.png" width="500"></p>
    - Do not need to search the right hand side of tree since 14 < 15