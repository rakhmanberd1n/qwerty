class Shape:
    def __init__(self, length, width): # он брался как стринг вот и потребовалось его за "инт"ить
        self.length = int(length)
        self.width = int(width)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        print("Here is the area of the rectangle: ", self.length*self.width)
plosh = Rectangle(input("give me the length of the rectangle: "), input("give me the width of the rectangle: "))
plosh.area()