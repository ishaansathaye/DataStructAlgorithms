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

    # while partition_index < len(elements) and elements[partition_index] < pivot:
    #     partition_index += 1
    
    # i_counter = partition_index

    # while i_counter < len(elements) and elements[i_counter] > pivot:
    #     i_counter += 1

    # swap(i_counter, partition_index, elements)

    return partition_index

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
    if len(elements) == 1:
        return
    if start < end:
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