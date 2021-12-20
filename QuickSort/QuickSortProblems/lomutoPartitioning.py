# Exercise: Quick Sort
# Implement quick sort using Lomuto partition scheme. 
# This partition scheme is explained in the video tutorial, you need to write python code to implement it. 
# Check the pseudo code here: https://en.wikipedia.org/wiki/Quicksort Check the section Lomuto partition scheme

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def lomuto_partition(elements, start, end):
    pivot = elements[end] #pivot is the end element
    partition_index = start #p index or partition index is the starting element index

    for i_counter in range(start, end): #keeps moving i counter
        if elements[i_counter] <= pivot: #i counter moves until element found that is less than pivot
            swap(i_counter, partition_index, elements) #if above statement found then swaps i counter element and p index element
            partition_index += 1 #keeps moving p index until element found that is greater than pivot
    
    swap(partition_index, end, elements) #swaps the p index element with the end element

    return partition_index

def quick_sort(elements, start, end): 
    if len(elements) == 1:
        return
    if start < end:
        pi = lomuto_partition(elements, start, end)
        quick_sort(elements, start, pi-1) 
        quick_sort(elements, pi+1, end)

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 3, 15, 28]
    quick_sort(elements, 0, len(elements)-1) #NOTE: use debugger to see quicksort recursion
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print("Sorted array:", elements)