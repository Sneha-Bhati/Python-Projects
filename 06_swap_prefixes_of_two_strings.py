# Practical 06: Swap prefixes of two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
k = int(input("Enter prefix length to swap: "))

if k < 0 or k > min(len(s1), len(s2)):
    print("Prefix length must be between 0 and the length of the shorter string.")
else:
    new_s1 = s2[:k] + s1[k:]
    new_s2 = s1[:k] + s2[k:]
    print("First string after swapping prefixes:", new_s1)
    print("Second string after swapping prefixes:", new_s2)
