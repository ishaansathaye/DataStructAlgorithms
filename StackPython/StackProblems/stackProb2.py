#Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def matches(ch1, ch2):
    dictMatches = {")": "(", "}": "{", "]": "["}
    return dictMatches[ch1] == ch2

def is_balanced(input):
    '''Makes stack object'''
    s = Stack()
    '''Goes through each character in input'''
    for char in input:
        '''Checks if the char equals the values in the dictionary'''
        if char == "(" or char == "[" or char == "{":
            '''Adds only these values to stack'''
            s.push(char)
        '''Checks if the char equals the key values in the dictionary'''
        if char == ")" or char == "]" or char == "}":
            '''Needs this to check if input starts with these values, which means nothing has been added to stack'''
            if s.size() == 0:
                '''Returns False if only key values start the input'''
                return False
            '''Compares char which is a key to s.pop() which is the value in the dictionary (also removes element from stack)'''
            if not matches(char, s.pop()):
                '''if does not match key then it becomes not False which is True -> returns False'''
                '''if does match key then it becomes not True which is False -> moves on'''
                return False
    '''returns True if every element has been popped or nothing has been added to stack'''
    '''returns False if there are still elements in stack'''
    return s.size() == 0

if __name__ == '__main__':
    print()
    print(is_balanced("({)}")) #False
    print(is_balanced("({a+b})")) #True
    print(is_balanced("))((a+b}{")) #False
    print(is_balanced("((a+b))")) #True
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    print()