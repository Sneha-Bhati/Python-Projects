# Practical 08: Print cubes of even integers in a range
start = int(input("Enter starting integer: "))
end = int(input("Enter ending integer: "))

if start > end:
    start, end = end, start

for number in range(start, end + 1):
    if number % 2 == 0:
        print(f"Cube of {number} = {number**3}")
