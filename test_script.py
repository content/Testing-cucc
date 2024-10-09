import pytest
from script import calculateSum, calculateDifference, calculateProduct, calculateQuotient

def test_calculateSum():
    assert calculateSum(2, 3) == 5
    assert calculateSum(0, 0) == 0
    assert calculateSum(-1, 1) == 0
    assert calculateSum(-1, -1) == -2
    
def test_calculateDifference():
    assert calculateDifference(3, 2) == 1
    assert calculateDifference(0, 0) == 0
    assert calculateDifference(-1, 1) == -2
    assert calculateDifference(-1, -1) == 0
    
def test_calculateProduct():
    assert calculateProduct(2, 3) == 6
    assert calculateProduct(0, 0) == 0
    assert calculateProduct(-1, 1) == -1
    assert calculateProduct(-1, -1) == 1
    
def test_calculateQoutient():
    assert calculateQuotient(6, 3) == 2
    assert calculateQuotient(0, 1) == 0
    assert calculateQuotient(-1, 1) == -1
    assert calculateQuotient(-1, -1) == 1