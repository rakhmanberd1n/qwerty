import math
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def show(self):
        print("There coordinates are : ", "x =", self.x, "y =",self.y)

    def move(self):
        self.x = input("Change x: ")
        self.y = input("Change y: ")

    def dist(self):
        self.sx = input("Write x coordinate for other point: ")
        self.sy = input("Write y coordinate for other point: ")
        distance = math.sqrt((int(self.sx)-int(self.x))**2 + (int(self.sy)-int(self.y))**2)
        print("The distance between two coordinates is: ", distance)

ball = Point(input("Write coordinates for x: "), input("Write coordinates for y: "))

ball.show()
ball.move()
ball.show()
ball.dist()