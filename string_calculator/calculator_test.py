from calculator import add
import pytest

def test_empty_string():
 assert(add("")) == 0

def test_one_intiger():
     assert(add("1")) == 1

    #two intigers
def test_two_intigers():
    assert(add("1,1")) == 2S

    #multiple intigers,
def test_multiple_intigers():
    assert(add("1,2,3,4")) == 10

    #handle new lines
def test_handle_new_lines:
    assert(add("1\n2,3")) == 6




