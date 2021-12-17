def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1 #convention if number not found

def binary_search(numbers_list, number_to_find):
    left_index = 0 #set left side index
    right_index = len(numbers_list) - 1 #set right side index
    mid_index = 0 #initial middle index

    while left_index <= right_index: #keep repeating while the left and right index are getting closer and closer (less than or equal to each other)
        mid_index = (left_index + right_index) // 2 #use floor for non integer values returned
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find: #wanted value found
            return mid_index
        
        if mid_number < number_to_find: #the middle number is less than wanted value -> number on right side of middle number
            left_index = mid_index + 1 #set left index to 1 more than the middle number index
        else: #the middle number is greater than wanted value -> number on left side of middle number
            right_index = mid_index - 1 #set right index to 1 less than the middle number index

    return -1 #if number not  found


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    
    number_to_find = 45
    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")

    print()
    
    number_to_find = 24
    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")

    print()

    number_to_find = 1000
    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")
