print()
def getsqrnum(num):
    '''this has time complexity of order n'''
    sqrnum = []
    for n in num:
        sqrnum.append(n*n)
    return sqrnum
    

numbers = [2,5,8,9]
print(getsqrnum.__doc__)
print(getsqrnum(numbers))
#[4, 25, 64, 81]
print()

