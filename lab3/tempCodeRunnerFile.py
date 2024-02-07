class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area of the shape:", 0)
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
        print("are of the rectangle:", self.length * self.width)
        
length = float(input())
width = float(input())
rectangle = Rectangle(length, width)
rectangle.area