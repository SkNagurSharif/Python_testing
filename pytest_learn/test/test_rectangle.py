import pytest
import dev.Shape as Shape
from pytest_learn.test.conftest import defered_rectangle, test_rectangle

# with fixture
"""
@pytest.fixture
def test_rectangle():
    return Shape.Rectangle(20,30)
"""

def test_rect_area(test_rectangle):
    assert test_rectangle.area() == 20*30
    
def test_rect_peri(test_rectangle):
    assert test_rectangle.perimeter() == (2*20)*(2*30)
        
# Without fixture        

def test_rect_Area():
    rectangle = Shape.Rectangle(20,30)
    assert rectangle.area() == 20*30
    
def test_rect_Peri(test_rectangle):
    rectangle = Shape.Rectangle(20,30)
    assert rectangle.perimeter() == (2*20)*(2*30)

def test_defered_reactangle():
    assert test_rectangle != defered_rectangle