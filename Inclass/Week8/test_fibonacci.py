
#In class activity
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def Fibonacci_test(n):
    if n < 0:
        # error
        print("INVALID INPUT")
    elif n == 0:
        # get 0
        return 0
    elif n == 1 or n == 2:
        # get 1
        return 1
    else:
        # get real value of fibonacci
        return Fibonacci_test (n-1) + Fibonacci_test (n-2)

def Factorial_test(n):
    if n == 1:
        return n
    elif n < 1:
        return "Error input (Negate Number)"
    else:
        return n * Factorial_test(n-1)
print (Fibonacci_test(10))
## Should be 55

print (Factorial_test(5))
## Should be 120
