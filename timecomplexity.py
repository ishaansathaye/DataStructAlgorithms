#Order of n: O(n)
#Depends on number of iterations
print('---------------------------')
def getsqrnum(num):
    '''this has time complexity of order n'''
    sqrnum = []
    for n in num:
        sqrnum.append(n*n)
    return sqrnum
numbers = [2,5,8,9]
print(getsqrnum(numbers))
print()

#Order of 1: O(1)
#Increasing input still means constant time
def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe
#doing a constant operation
#does not matter about the size of eps
#time execution remains constrant

#order of n^2: 0(n^2)
newset = [3,6,2,4,3,6,8,9]
for i in range(len(newset)):
    for j in range(i+1, len(newset)):
        if newset[i] == newset[j]:
            print(newset[i] + " is a duplicate")
            break
#time = a*n^2 + b
#Keep fastest frowing term and drop constants ->
#

