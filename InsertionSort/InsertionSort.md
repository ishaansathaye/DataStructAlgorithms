## Insertion Sort
---
### Theory - How Bubble Sort works
- Example: <p align="center"><img src="Images/bubble.png" height="300"></p>
1) If first element in greater than second element -> swap
2) Compare second element with third -> swap if second greater
3) Keep repeating until the **highest number is at the end**
4) Repeat above steps again until entire dataset is sorted
- Summary
    - Highest number goes towards the end
    - Comparing side by side elements
- *Why it is called bubble sort:*
    - Like bubbles rise to the top, highest number goes to the correct position
### Space-Time
- Time Complexity: **O(n^2)**
- Space Complexity: **O(1)**
    - Not using any additional space -> just using the same list