from abc import ABCMeta , abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    
    def area(self):
        return 0
    




class Rectange(Shape):
    type = "rectange"
    side = 4
    
    
    def __init__(self):
        self.length = 16
        self.breadth = 11
        
        
    def area(self):
        return self.length * self.breadth
    
rect1 = Rectange()  
print(rect1.area)