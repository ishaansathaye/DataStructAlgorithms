#Original Selection Sort
# def selection_sort(arr):
#     for i in range(0, len(arr)):
#         minElem = arr[i]
#         saveJ = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < minElem:
#                 minElem = arr[j]
#                 saveJ = j
#         arr[i], arr[saveJ] = minElem, arr[i]

#codebasics selection sort
def find_min_element(arr):
    min = 10000000
    for i in range(arr):
        if arr[i] < min:
            min = arr[i]
    return min

def selection_sort(arr):
    size = len(arr)
    for i in range(size-1): #no need to go all the way to the last element
        min_index = i #set the min index as the counter i
        for j in range(min_index+1, size): #go through list again starting from i+1 element
            if arr[j] < arr[min_index]: #if the current element is less than the ith element
                min_index = j #min index becomes the j index
        if i != min_index: #if i element already is the min element then no need to swap
            arr[i], arr[min_index] = arr[min_index], arr[i] #swap the ith element with the min_index element


if __name__ == '__main__':
    elements = [78, 12, 15, 8, 61, 53, 23, 27]
    selection_sort(elements)
    print(elements)

    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)