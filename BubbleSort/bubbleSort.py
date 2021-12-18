def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1): #repeating swapping process n-1 times
        swapped = False #variable for checking if list is already swapped -> do not need to keep iterating 
        for j in range(size-1-i): #swappig pairs in list, -i is if elements have been sorted do not need to compare those again (saving time)
            if elements[j] > elements[j+1]: #in pair, if first greater than second -> swap
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped: #checks if swapped has not happened - False
            break #break the outer loop
    
    return elements


if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    print(bubble_sort(elements))

    print()

    elements = [1, 2, 4] #need to check if list is already sorted
    print(bubble_sort(elements))

    #bubble sort also works on strings -> for python
