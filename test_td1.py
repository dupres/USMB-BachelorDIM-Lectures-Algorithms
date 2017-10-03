import td1

def test_remove_whitespaces_a_b():
    assert td1.remove_whitespaces("a b") == "ab"
    
def test_remove_whitespaces_ab():
    assert td1.remove_whitespaces("ab") == "ab"
    
def test_remove_whitespaces_a():
    assert td1.remove_whitespaces(" a ") == "a"
    
def test_remove_whitespaces_empty():
    assert td1.remove_whitespaces(" ") == ""

def test_remove_whitespaces__a_b_():
    assert td1.remove_whitespaces(" a b ") == "ab"    
    
def test_list_max():
    assert td1.list_max([1,2,3]) == (3,2)
