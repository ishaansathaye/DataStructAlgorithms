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
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index
def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index]+[key]+array[index:]

if __name__ == '__main__':
    elements  = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(elements)
    
    print()
    
    #codebasics solution - uses input of elements in list
    stream = []
    count = 0
    while(True):
        i = int(input())
        count += 1
        stream = insertion_sort(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")