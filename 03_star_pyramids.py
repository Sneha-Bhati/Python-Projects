# Practical 03: Display star pyramid patterns
rows = int(input("Enter number of rows: "))

print("\\nCentered pyramid:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print("\\nInverted pyramid:")
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

print("\\nRight-angled triangle:")
for i in range(1, rows + 1):
    print("* " * i)
