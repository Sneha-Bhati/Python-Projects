# Practical 10: Create a dictionary of numbers and their cubes
n = int(input("How many integers? "))
cubes = {}

for _ in range(n):
    number = int(input("Enter an integer: "))
    cubes[number] = number**3

print("Dictionary of cubes:", cubes)
