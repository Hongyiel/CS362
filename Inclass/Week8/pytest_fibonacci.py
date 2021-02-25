import pytest
from fibonacci import *
def test_case1():
    assert Fibonacci(3) == 2
    assert Factorial(3) == 6

## IMPORTANT README ##

# I made Exception on the fibonacci.py so it will not show error raise
# if there are error on the code.
def test_case2():
    # String type will raise Exception on this
    with pytest.raises(TypeError):
        Factorial("r")
        Fibonacci("r")

def test_case3():
    assert Fibonacci(4) == 3
    assert Fibonacci("dd") == 2
    #ERROR CASE


def test_case4():
    assert Factorial("ss") == 6
    #ERROR CASE
    assert Factorial(3) == 6

## IMPORTANT README ##

# I made Exception on the fibonacci.py so it will not show error raise
# if there are error on the code.
def test_case5():
    # String type will raise Exception on this
    with pytest.raises(TypeError):
        Factorial("r")
