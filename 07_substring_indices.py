# Practical 07: Find the indices of a substring
text = input("Enter the main string: ")
sub = input("Enter the substring to search: ")

if sub == "":
    print("An empty substring occurs at every index from 0 to", len(text))
else:
    indices = []
    start = 0
    while True:
        index = text.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # Also finds overlapping occurrences.
    if indices:
        print("Substring found at indices:", indices)
    else:
        print("Substring not found.")
