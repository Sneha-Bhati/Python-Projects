# Practical 01: Roots of a Quadratic Equation
# Solves ax^2 + bx + c = 0 using the discriminant.
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    if b == 0:
        print("Not a valid equation." if c != 0 else "Infinitely many solutions.")
    else:
        print("Linear equation root:", -c / b)
else:
    d = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
