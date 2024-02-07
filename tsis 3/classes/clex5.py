class Shape:
    def __init__(self, length = 0): # он брался как стринг вот и потребовалось его за "инт"ить
        self.length = int(length)

    def area(self):
        return self.length*0

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    def area(self):
        print("Here is the area of the square: ", self.length*self.length)
plosh = Square(input("give me the length of the square: "))
plosh.area()