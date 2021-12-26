#iterative approach
def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

#NOTE: use debugger to see call stackand stack unwinding

#recursive approach
def recursive_find_sum(n):
    sum = 0
    if n > 0:
        sum = n+recursive_find_sum(n-1)
    return sum #terminates when base condition of n=1 is met -> returns the sum of 1

#Fibonacci problem
def fib(n): #fibonacci number at nth position
    if n == 0 or n == 1:
        return n
    return fib(n-1)+fib(n-2)
    


if __name__ == '__main__':
    print(find_sum(5)) #15
    print(recursive_find_sum(5)) #15
    print(fib(4))