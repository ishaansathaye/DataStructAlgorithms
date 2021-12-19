def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

#need start and end for recursion
def partition(elements, start_pointer, end_pointer): #creates a partition by putting an element in the correct position and create left and right sides
    pivot_index = start_pointer
    pivot = elements[pivot_index]

    while start_pointer < end_pointer: #keeps process going until the pointers cross
        while elements[start_pointer] <= pivot: #do until found element greater than pivot
            start_pointer += 1 #keep moving start pointer

        while elements[end_pointer] > pivot: #do until found element less than pivot
            end_pointer -= 1
        
        if start_pointer < end_pointer: #do not want to swap two pointers when pointers cross
            swap(start_pointer, end_pointer, elements) #swap start and end elements
    
    swap(pivot_index, end_pointer, elements) #swaps end pointer and pivot if the pointers cross

    return end_pointer #position of the pivot at the end of partitioning

#need start and end for recursion
def quick_sort(elements, start_pointer, end_pointer): #Hoare Partitioning Method used
    if start_pointer < end_pointer: #keep repeating process until start and end are equal which means that it is sorted
        pi = partition(elements, start_pointer, end_pointer) #partition index
        quick_sort(elements, start_pointer, pi-1) #run quick sort on left partition
        quick_sort(elements, pi+1, end_pointer) #run quick sort on right partition

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 3, 15, 28]
    print(quick_sort(elements, 0, len(elements)-1))