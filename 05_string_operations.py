# Practical 05: Common string operations
text = input("Enter a string: ")

print("Original string:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Reversed:", text[::-1])
print("Number of vowels:", sum(1 for ch in text.lower() if ch in "aeiou"))
print("Number of words:", len(text.split()))
