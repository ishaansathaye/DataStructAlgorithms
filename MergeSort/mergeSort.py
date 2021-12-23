def merge_sort(arr): #recursive function - need to take care of exit condition first (whenever arr of size 1)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #gives the midpoint of arr
    
    left = arr[:mid] #dividing arr using midpoint
    right = arr[mid:]

    left = merge_sort(left) #recursion on left side of divided arr
    right = merge_sort(right) #recursion on right side of divided arr

    return merge_two_sorted_lists(left, right) #recursively returns one list merged with sorted lists


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
    print(merge_sort(arr))