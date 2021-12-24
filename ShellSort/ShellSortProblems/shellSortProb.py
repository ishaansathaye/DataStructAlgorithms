# Sort the elements of a given list using shell sort, but with a slight modification. 
# Remove all the repeating occurrences of elements while sorting.

# Traditionally, when comparing two elements in shell sort, we swap if first element is bigger than second, and do nothing otherwise.

# In this modified shell sort with duplicate removal, we will swap if first element is bigger than second, and do nothing if element is smaller, 
# but if values are same, we will delete one of the two elements we are comparing before starting the next pass for the reduced gap.

# For example, given the unsorted list [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3], after sorting using shell sort without duplicates, the sorted list would be:
# [0, 1, 2, 3, 5, 7, 8, 9]

def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2
            

if __name__ == '__main__':
    unsorted_duplicate_arr = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    shell_sort(unsorted_duplicate_arr)
    print(unsorted_duplicate_arr)