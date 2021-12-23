#NOTE: use debugger to see recursion with merge_sort and merge_two_sorted_lists2
def merge_sort(arr): #recursive function - need to take care of exit condition first (whenever arr of size 1)
    if len(arr) <= 1: #if single element array
        return

    mid = len(arr) // 2 #gives the midpoint of arr
    left = arr[:mid] #dividing arr using midpoint
    right = arr[mid:]

    merge_sort(left) #recursion on left side of divided arr
    merge_sort(right) #recursion on right side of divided arr

    merge_two_sorted_lists2(left, right, arr) #recursively returns one list merged with sorted lists
    #sorts array in line

def merge_two_sorted_lists2(a, b, arr): #Approach 2: without using separate list (optimizes memory usage)
    len_a, len_b = len(a), len(b)
    i = j = k = 0 #k is the index for the sorted arr

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i] #adding element to the list arr
            i += 1
        else:
            arr[k] = b[j]
            j += 1 
        k += 1 #incrementing index of arr
        
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def merge_two_sorted_lists(a, b): #Approach 1: with two sorted lists, merge into 1 sorted list
    sorted_list = [] #new empty sorted list
    len_a, len_b = len(a), len(b) #lengths of arrays
    i = j = 0 #counters

    while i < len_a and j < len_b: #keep going until counter has reached the length of a and b
        if a[i] <= b[j]: #compare element of a with element of b -> if it is smaller
            sorted_list.append(a[i]) #append the element to the new sorted list
            i += 1 #increment a counter 
        else:
            sorted_list.append(b[j])
            j += 1 #increment b counter
        
    #takes care of problem of not appending last elements and uneven lengths of lists 
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list

if __name__ == '__main__':
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]
    print(merge_two_sorted_lists(a, b))

    print()

    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(arr)
    print(arr)

    print()

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    for arr in test_cases:
        merge_sort(arr)
        print(arr)