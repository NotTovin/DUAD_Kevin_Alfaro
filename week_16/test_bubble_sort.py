import pytest
from bubble_sort import bubble_sort

def test_small_list():
    #Arrange
    small_list = [1,5,7]
    #Act
    result = bubble_sort(small_list)
    #Assert
    assert result 

def test_large_list():
    #Arrange
    large_list = list(range(1, 101))
    #Act
    result = bubble_sort(large_list)
    #Assert
    assert result
    


def test_empty_list():
    #Arrange
    empty_list = []
    #Act
    result = bubble_sort(empty_list)
    #Assert
    assert result == []
    

def test_invalid_input():
    #Arrange
    email_input = 'test@gmail.com'
    #Act#Assert
    with pytest.raises(TypeError):
        bubble_sort(email_input)
    