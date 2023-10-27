import pytest
import dev.my_fun as fun

def test_add():
    res = fun.add(20,21)
    assert res == 41

def test_mul():
    res = fun.mul(20,21)
    assert res == 420
    
def test_div_by_zero():
    
    # Handling Exception Error
    #Zero division error   
    # Way 1
    #res = fun.div(82,0)
    #assert res == 82
    with pytest.raises(ZeroDivisionError):
        fun.div(82,0)
        
# Adding Strings
def test_add_Strings():
    res = fun.add("Hello ","to Me")
    assert res == "Hello to Me"
