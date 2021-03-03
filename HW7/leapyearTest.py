import pytest
from leapyearImp import *
def Error():
    raise ValueError

def test_case1():
    # String type will raise Exception on this
    get_result("r")
    # if get string
    with pytest.raises(ValueError):
            Error()
# if input number
def test_case2():
    get_result(1000)
    with pytest.raises(ValueError):
            Error()
# if negate number
def test_case3():
    get_result(-23)
    with pytest.raises(ValueError):
            Error()
