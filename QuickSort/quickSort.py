def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements): #creates a partition by putting an element in the correct position and create left and right sides
    pivot_index = 0
    pivot = elements[pivot_index]

    start_pointer = pivot_index+1
    end_pointer = len(elements) - 1

    while start_pointer < end_pointer: #keeps process going until the pointers cross
        while elements[start_pointer] <= pivot: #do until found element greater than pivot
            start_pointer += 1 #keep moving start pointer

        while elements[end_pointer] > pivot: #do until found element less than pivot
            end_pointer -= 1
        
        if start_pointer < end_pointer: #do not want to swap two pointers when pointers cross
            swap(start_pointer, end_pointer, elements) #swap start and end elements
    
    swap(pivot_index, end_pointer, elements) #swaps end pointer and pivot if the pointers cross

    return elements




def quick_sort(elements): #Hoare Partitioning Method used
    return partition(elements)

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 3, 15, 28]
    print(quick_sort(elements))