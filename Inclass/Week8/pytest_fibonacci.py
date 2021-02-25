import pytest
from fibonacci import *
def test_case1():
    assert Fibonacci(3) == 2

def test_case2():
    # String type will raise Exception on this
    with pytest.raises(TypeError):
        Fibonacci("r")

def test_case3():
    assert Factorial(3) == 6

def test_case4():
    # String type will raise Exception on this
    with pytest.raises(TypeError):
        Factorial("r")
