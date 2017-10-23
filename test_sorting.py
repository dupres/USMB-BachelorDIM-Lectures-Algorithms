import sorting
import numpy

def test_selective_sort_1_2_3_asc():
    assert sorting.selective_sort([1,2,3],"asc") == [1,2,3];

def test_selective_sort_1_2_3_desc():
    assert sorting.selective_sort([1,2,3],"desc") == [3,2,1];

def test_selective_sort_3_2_1_asc():
    assert sorting.selective_sort([3,2,1],"asc") == [1,2,3];

def test_selective_sort_3_2_1_desc():
    assert sorting.selective_sort([3,2,1],"desc") == [3,2,1];

def test_selective_sort_0_1_m1_desc():
    assert sorting.selective_sort([0,1,-1],"desc") == [1,0,-1];

def test_selective_sort_0_asc():
    assert sorting.selective_sort([0],"asc") == [0];

def test_selective_sort_m3_m2_m1_asc():
    assert sorting.selective_sort([-3,-2,-1],"asc") == [-3,-2,-1];

def test_selective_sort_m3_m2_m1_desc():
    assert sorting.selective_sort([-3,-2,-1],"desc") == [-1,-2,-3];