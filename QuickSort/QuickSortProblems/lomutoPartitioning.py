# Exercise: Quick Sort
# Implement quick sort using Lomuto partition scheme. 
# This partition scheme is explained in the video tutorial, you need to write python code to implement it. 
# Check the pseudo code here: https://en.wikipedia.org/wiki/Quicksort Check the section Lomuto partition scheme

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def lomuto_partition(elements, start, end):
    pivot_index = end
    pivot = elements[pivot_index]

    partition_index = elements[start]

    while partition_index < len(elements) and elements[partition_index] < pivot:
        partition_index += 1
    
    i_counter = partition_index

    while i_counter < len(elements) and elements[i_counter] > pivot:
        i_counter += 1

    swap(i_counter, partition_index, elements)

    return i_counter

    # while start_pointer < end_pointer: 
    #     while start_pointer < len(elements) and elements[start_pointer] <= pivot: 
    #         start_pointer += 1 

    #     while elements[end_pointer] > pivot:
    #         end_pointer -= 1
        
    #     if start_pointer < end_pointer: 
    #         swap(start_pointer, end_pointer, elements)
    
    # swap(pivot_index, end_pointer, elements)

    # return end_pointer


def quick_sort(elements, start, end): 
    if start >= end or start < 0:
        return
    pi = lomuto_partition(elements, start, end)
    quick_sort(elements, start, pi-1) 
    quick_sort(elements, pi+1, end)

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 3, 15, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    # tests = [
    #     [11,9,29,7,2,15,28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]

    # for elements in tests:
    #     quick_sort(elements, 0, len(elements)-1)
    #     print(f'Sorted array: {elements}')