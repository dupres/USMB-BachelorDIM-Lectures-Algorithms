import td1
import numpy

def test_remove_whitespace_a_b():
    assert td1.remove_whitespace("a b") == "ab"
    
def test_remove_whitespace_ab():
    assert td1.remove_whitespace("ab") == "ab"
    
def test_remove_whitespace_a():
    assert td1.remove_whitespace(" a ") == "a"
    
def test_remove_whitespace_empty():
    assert td1.remove_whitespace(" ") == ""

def test_remove_whitespace__a_b_():
    assert td1.remove_whitespace(" a b ") == "ab"    
    
def test_max_value_1_2_3():
    assert td1.max_value([1,2,3]) == (3,2)

# def test_max_value_empty():
    # assert td1.max_value([]) == -1
	
def test_max_value_3_2_1():
    assert td1.max_value([3,2,1]) == (3,0)

def test_max_value_m1_m5():
    assert td1.max_value([-1,-5]) == (-1,0)

def test_average_above_zero_0_m1_2():
	assert td1.average_above_zero([1,2,0]) == [2,1,1]
	
def test_average_above_zero_m1():
	assert td1.average_above_zero([-1]) == [0,1,-1]

def test_roi_bbox():
	assert td1.roi_bbox([[0,0,0],[0,1,0],[0,0,0]]).all() == numpy.array([[1,1],[1,1]]).all()

