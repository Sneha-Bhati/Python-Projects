# Practical 14: Inheritance - class Point3D extends Point2D
import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"2D Point: ({self.x}, {self.y})")


class Point3D(Point2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"3D Point: ({self.x}, {self.y}, {self.z})")

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
z = float(input("Enter z-coordinate: "))

point = Point3D(x, y, z)
point.display()
print("Distance from origin:", point.distance_from_origin())
