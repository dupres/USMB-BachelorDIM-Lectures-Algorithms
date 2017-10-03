import td1

def test_remove_whitespaces():
    assert td1.remove_whitespaces("a b") == "ab"
    
def test_list_max():
    assert td1.list_max([1,2,3]) == [3,2]
