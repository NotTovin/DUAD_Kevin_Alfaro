class Circle():
    
    pi = 3.141592653589793
    
    def __init__(self, radius):
        self.radius =  radius
        
    
    def get_area(self):
        self.total_area =  self.pi * (self.radius ** 2)
        print(f'The area of the circle is {self.total_area}')
    
my_circle_1 = Circle(56)
print(my_circle_1.get_area())
