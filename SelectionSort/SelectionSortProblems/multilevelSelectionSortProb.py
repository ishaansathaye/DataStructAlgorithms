# Implement a Multi-Level Sort of a given list of dictionaries based on a given sorting order. 
# If user wants to sort dictionary based on First Key 'A', Then Key 'B', they shall pass list of keys in the order of preference as a list ['A','B']. 
# Your code should be able to sort list of dictionaries for any number of keys in sorting order list.

# Using this multi-level sort, you should be able to sort any list of dictionaries based on sorting order preference

# Example: A single dictionary entry contains two keys 'First Name' and 'Last Name'. 
# The list should be sorted first based on 'First Name', then based on 'Last Name', w.r.t. common/same 'First Name' entries.

# For this, one shall past sorting order of preference list [ 'First Name' , 'Last Name' ]
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/7_SelectionSort/selection_sort_exercise.md


def multilevel_selection_sort(arr, preference):
    size = len(arr)
    for key in preference[::-1]: #reversing preference list in order to first sort by first name and then last name (look at output)
        for i in range(size-1):
            min_index = i
            for j in range(min_index+1, size): 
                if arr[j][key] < arr[min_index][key]:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    multilevel_selection_sort(elements, ["First Name", "Last Name"])
    for dict in elements:
        print(dict)