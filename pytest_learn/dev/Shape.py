import math


class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class circles(Shape):
    def __init__(self,radius):
        self.rad = radius
        
    def area(self):
        return math.pi*self.rad**2
    
    def perimeter(self):
        return 2*math.pi*self.rad    
    
class Rectangle(Shape):
    
    def __init__(self,length, width):
        self.length = length
        self.width =width
        
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return (2*self.length)*(self.width*2)
    