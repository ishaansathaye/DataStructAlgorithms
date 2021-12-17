# 1. When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
# numbers = [1,4,6,9,10,5,7]
# Answer: The list is not sorted so that means that it will find the middle number and find that 9 > 5 so it will check the left side of the list.
# The left side of the list does not have the wanted number

#Find index of all the occurrences of a number from sorted list
numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  
# This should return 5,6,7 as indices containing number 15 in the array

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1 # number not found

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
            left_index = mid_index + 1
    else: 
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def find_occurrences(numbers_list, number_to_find):
    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    indices = [index]

    i = index - 1 #check left side of the list for more occurrences
    while i >= 0:
        if numbers_list[i] == number_to_find:
            indices.append(i)
        i = i - 1
    
    i = index + 1 #check right side of the list for more occurrences
    while i < len(numbers_list):
        if numbers_list[i] == number_to_find:
            indices.append(i)
        i = i + 1
    
    indices.sort()
        
    return indices
    
print(find_occurrences(numbers, number_to_find))
