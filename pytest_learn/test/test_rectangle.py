import pytest
import dev.Shape as Shape

# with fixture
@pytest.fixture

def Test_Rectangle():
    return Shape.Rectangle(20,30)

def test_rect_area(Test_Rectangle):
    assert Test_Rectangle.area() == 20*30
    
def test_rect_peri(Test_Rectangle):
    assert Test_Rectangle.perimeter() == (2*20)*(2*30)
        
# Without fixture        

def test_rect_Area():
    rectangle = Shape.Rectangle(20,30)
    assert rectangle.area() == 20*30
    
def test_rect_Peri(Test_Rectangle):
    rectangle = Shape.Rectangle(20,30)
    assert rectangle.perimeter() == (2*20)*(2*30)
