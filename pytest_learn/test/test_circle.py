import math
import pytest
import dev.Shape as Shape
from pytest_learn.test.conftest import test_rectangle

class TestCircle:
            
    # setup method run first before each test method
    
    def setup_method(self,method):
        print(f" This is a setup {method} ")
        self.circle = Shape.circles(20)
    
    def teardown_method(self, method):
        print(f" This is Tear down {method}")   
        del self.circle 
    
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.rad**2
    
    def test_perimeter(self):
        assert self.circle.perimeter() == math.pi*2*self.circle.rad
        
    def test_not_def_rectangle(self,test_rectangle):
        assert self.circle.area() != test_rectangle
