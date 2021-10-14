print()
print("Order of n: O(n):")
print('---------------------------')
def getsqrnum(num):
    sqrnum = []
    for n in num:
        sqrnum.append(n*n)
    return sqrnum
numbers = [2,5,8,9]
print(getsqrnum(numbers))
print("Depends on number of iterations")
print("This has time complexity of order n")
print('---------------------------')

print()
print("Order of 1: O(1):")
print('---------------------------')
def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe
print("Increasing input still means constant time")
print("Doing a constant operation")
print("Does not matter about the size of eps")
print("Time execution remains constrant")
print('---------------------------')

print()
print("Order of n^2: 0(n^2):")
print('---------------------------')
newset = [3,6,2,4,3,6,8,9]
for i in range(len(newset)):
    for j in range(i+1, len(newset)):
        if newset[i] == newset[j]:
            print(str(newset[i]) + " is a duplicate")
            break
print("time = a*n^2 + b")
print("Keep fastest frowing term and drop constants ->")
print("Becomes 0(n^2)")
print('---------------------------')

print()
print("Order of n^2: 0(n^2):")
print('---------------------------')
print("Below has n^2 iterations")
newNumbers = [3,6,2,4,3,6,8,9]
duplicate = None
for i in range(len(newNumbers)):
    for j in range(i+1, len(newNumbers)):
        if newNumbers[i] == newNumbers[j]:
            duplicate = newNumbers[i]
            break
print("Below has n iterations")
for i in range(len(newNumbers)):
    if newNumbers[i] == duplicate:
        print(i)
print("time = a*n^2 + b*n + c")
print("Use rules and keep fastest growing and drop constants ->")
print("Becomes 0(n^2)")
print('---------------------------')