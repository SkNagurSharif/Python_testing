import pytest
import dev.Shape as Shape

@pytest.fixture

def Test_Rectangle():
    return Shape.Rectangle(20,30)

def test_rect_area(Test_Rectangle):
    assert Test_Rectangle.area() == 20*30
    
def test_rect_peri(Test_Rectangle):
    assert Test_Rectangle.perimeter() == (2*20)*(2*30)
        