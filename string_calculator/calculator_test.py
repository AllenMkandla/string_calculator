from calculator import add
import pytest

def test_empty_string():
    assert(add("")) == 0

def test_one_intiger():
     assert(add("1")) == 1

#two intigers
def test_two_intigers():
    assert(add("1,1")) == 2

    #multiple intigers,
def test_multiple_intigers():
    assert(add("1,2,3,4")) == 10

    #handle new lines
def test_handle_new_lines():
    assert(add("1\n2,3")) == 6

# handle different delimeters
def test_first_case_delimeter_exception():
    assert(add("//;\n1;2")) == 3

def test_negative_num_exception():
    with pytest.raises(Exception) as negative:
        assert(negative.add("-1,-2,3,4")) == "ERROR: negatives not allowed -1,-2"

def test_greater_than_1000():
    assert(add("//;\n1000,1;2")) == 3

def test_delimeters_of_any_length():
    assert (add("//***\n1***2***3")) == 6

def test_different_delimeters():
    assert(add("//[:D][%]\n1:D2%3")) == 6

def test_different_delimeters():
    assert(add("//[***][%%%]\n1***2%%%3")) == 6

def test_different_delimeters():
   assert(add("//[(-_-')][%]\n1(-_-')2%3")) == 6

