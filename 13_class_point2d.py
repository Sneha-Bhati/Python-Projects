# Practical 13: Class Point2D
import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point: ({self.x}, {self.y})")

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

p1 = Point2D(x1, y1)
p2 = Point2D(x2, y2)

p1.display()
p2.display()
print("Distance of first point from origin:", p1.distance_from_origin())
print("Distance between the points:", p1.distance_to(p2))
