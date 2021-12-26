#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

print()
# 1. Write a Python program to calculate the sum of a list of numbers.  
def solution(listofnum, index):
    if index == len(listofnum)-1:
        return listofnum[index]
    return listofnum[index]+solution(listofnum, index+1)

print(solution([2, 4, 5, 6, 7], 0))

def alt_solution(listofnum):
    if len(listofnum) == 1: #when the length of list reaches 1
        return listofnum[0] #returns last element left after removing all elements
    else:
        return listofnum[0] + alt_solution(listofnum[1:]) # [1:] removes the first element in the list

print(alt_solution([2, 4, 5, 6, 7]))

print()

# 2. Write a Python program to converting an Integer to a string in any base.
def alt_solution2(n, base):
    conver_tString = "0123456789ABCDEF"
    if n < base:
        return conver_tString[n]
    else:
        return alt_solution2(n // base, base) + conver_tString[n % base]

print(alt_solution2(2835, 16))

print()

# 3. Write a Python program of recursion list sum.  
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
def alt_solution3(listThings):
    sumList = 0
    for element in listThings:
        if type(element) == type([]):
            sumList += alt_solution3(element)
        else:
            sumList += element
    return sumList

print(alt_solution3([1, 2, [3,4], [5,6]]))

print()

# 4. Write a Python program to get the factorial of a non-negative integer.
def solution4(n):
    if n == 0:
        return 1
    return n*solution4(n-1)

print(solution4(4))

print()

# 5. Write a Python program to solve the Fibonacci sequence using recursion.  
def solution5(n):
    if n == 0 or n == 1:
        return n
    return solution5(n-1) + solution5(n-2)

print(solution5(7))

def alt_solution5(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (alt_solution5(n - 1) + (alt_solution5(n - 2)))

print(alt_solution5(7))

print()

# 6. Write a Python program to get the sum of a non-negative integer.
# Test Data: 
# sumDigits(345) -> 12
# sumDigits(45) -> 9 
def alt_solution6(n):
    if n == 0:
        return 0
    return n % 10 + alt_solution6(n // 10) #adding the last number (gotten by taking remainder of dividing by 10) and adding the 

print(alt_solution6(345))

# print(solution6(345))

# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
# Test Data: 
# sum_series(6) -> 12
# sum_series(10) -> 30 

# 8. Write a Python program to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers. 

# 9. Write a Python program to calculate the geometric sum of n-1.
# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms. 

# 10. Write a Python program to calculate the value of 'a' to the power 'b'.  
# Test Data : 
# (power(3,4) -> 81 


# 11. Write a Python program to find the greatest common divisor (gcd) of two integers.  