#In class activity
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# implementation fibonacci.py
import pytest
def Fibonacci(n):
    try:
        # Number will on here
        if n < 0:
            # error
            return "Error input (Negate number)"
        elif n == 0:
            # get 0
            return 0
        elif n == 1 or n == 2:
            # get 1
            return 1
        else:
            # get real value of fibonacci
            return Fibonacci (n-1) + Fibonacci (n-2)
    except Exception as e:
        return "ERROR this is not number"
def Factorial(n):
    try:
        # Number will on here
        if n == 1:
            return n
        elif n < 1:
            return "Error input (Negate Number)"
        else:
            return n * Factorial(n-1)
    except Exception as e:
        # If not number will here
        return "ERROR this is not number"
