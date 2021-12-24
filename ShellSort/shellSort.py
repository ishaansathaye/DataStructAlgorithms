#NOTE: Use debugger to visualize algo sorting sub-arrays created due to gaps
def shell_sort(arr):
    size = len(arr)
    gap = size // 2 #common way of finding gap

    while gap > 0: #continue for gap greater or equal to 1
        for i in range(gap, size): #makes the gap element the anchor (anything left of gap element should be sorted)
            anchor = arr[i] #set the anchor as starting with gap element
            j = i #create another counter j same as gap
            while j >= gap and arr[j-gap] > anchor: #compare element that is gap away from the left with anchor, j needs to be less than gap otherwise negative index
                arr[j] = arr[j-gap] #swap j=i element with the gap away element
                j -= gap #need to reduce j index by gap
            arr[j] = anchor #make the gap away element (which is j element since reduced) the anchor element
        gap = gap // 2 #reduce gap by n / 2 each time sorted with each gap
            

if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(elements)
    print(elements)

    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]

    for elements in tests:
        shell_sort(elements)
        print(elements)