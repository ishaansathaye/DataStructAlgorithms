# Compute the running median of a sequence of numbers. 
# That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2
def print_median(elements, length_left):
    if length_left % 2 == 0:
        first_num = elements[int((length_left/2)-1)]
        sec_num = elements[int((length_left/2))]
        median = (first_num + sec_num) / 2
    else:
        median = elements[int(length_left // 2)]
    print(median)

def insertion_sort(elements):
    print(elements[0])
    for i in range(1, len(elements)): 
        if i != 1:
            print_median(elements, i)
        anchor = elements[i] 
        j = i - 1 
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j] 
            j -= 1
        elements[j+1] = anchor
    print_median(elements, len(elements))

#codebasics solution
def place_to_insert(array, key):
    index = 0 #starts algo at first element
    for i in array: #iterates through current stream list
        if i > key: #if the new value is less than any elements
            break #gets out of loop to return the index it should insert at
        else:
            index += 1 #if the new value is greater than any elements -> keep increasing index to insert at
    return index #returns the index new value should be inserted at
def insert_to_sorted(array, key):
    index = place_to_insert(array, key) #gets index of where new value should be added in list
    return array[0:index]+[key]+array[index:] #returns list with added element in right position

if __name__ == '__main__':
    elements  = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(elements)
    
    print()
    
    #codebasics solution - uses input of elements in list
    #NOTE: use debugger to see algo in progress
    
    stream = [] #first approach of quicksort where using a separate list
    count = 0 #keeps track of number of elements in stream (for getting median)
    while(True):
        i = int(input())
        count += 1 #incrases count for each element added to stream
        stream = insert_to_sorted(stream, i) #calls second function on the current steam list with the new value i
        if count % 2 == 1: #below is the algo for finding median in current stream list
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")