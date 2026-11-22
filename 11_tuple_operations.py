# Practical 11: Tuple operations
values = tuple(input("Enter tuple elements separated by spaces: ").split())

print("Tuple:", values)
print("Length:", len(values))
if values:
    print("First element:", values[0])
    print("Last element:", values[-1])
    item = input("Enter an element to count: ")
    print("Count:", values.count(item))
    print("Index:", values.index(item) if item in values else "Element not present")
    print("As a list:", list(values))
else:
    print("The tuple is empty.")
