def insertion_sort(elements):
    for i in range(1, len(elements)): #consider the first element of list as sorted
        anchor = elements[i] #current element that the algo is dealing with (saves value to later insert)
        j = i - 1 #previous element of anchor
        while j >= 0 and anchor < elements[j]: # compares the anchor to every element on left side (if j less than 0 sets first element to the anchor)
            elements[j+1] = elements[j] #swapping the elements
            j -= 1
        elements[j+1] = anchor #set the swapped value to the anchor

#NOTE: use debugger to visualize how the algo works

if __name__ == '__main__':
    elements  = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)

    print()

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print('sorted array:', elements)