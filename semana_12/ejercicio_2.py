from abc import ABC, abstractmethod


class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
        print(f'Circle perimeter is {self.perimeter}')
    
    def calculate_area(self):
        self.area = 3.14 * self.radius ** 2
        print(f'Circle area is {self.area}')

class Square(Shape):
    
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        self.perimeter = self.side + self.side + self.side + self.side
        print(f'Square perimeter is  {self.perimeter}')
    
    def calculate_area(self):
        self.area =  self.side * self.side
        print(f'Area of the square is  {self.area}')

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        print(f'Rectangle perimeter is {self.perimeter}')
    
    def calculate_area(self):
        self.area  = self.width * self.height
        print(f'Area of the rectangle is {self.area}')
    
    

my_circle = Circle(5)
my_circle.calculate_perimeter()
my_circle.calculate_area()

my_square = Square(12)
my_square.calculate_area()
my_square.calculate_perimeter()

my_rectangle = Rectangle(12, 8)
my_rectangle.calculate_area()
my_rectangle.calculate_perimeter()