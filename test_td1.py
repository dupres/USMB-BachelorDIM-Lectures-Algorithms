import td1.py

def test_remove_whitespaces():
    assert remove_whitespaces("a b") == "ab"
    
def test_list_max():
    assert list_max([1,2,3]) == [3,2]
