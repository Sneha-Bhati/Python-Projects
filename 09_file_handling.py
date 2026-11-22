# Practical 09: Basic file handling (write, append, and read)
filename = input("Enter file name (for example notes.txt): ")

with open(filename, "w", encoding="utf-8") as file:
    content = input("Enter text to write to the file: ")
    file.write(content + "\\n")

more = input("Would you like to append another line? (y/n): ").strip().lower()
if more == "y":
    with open(filename, "a", encoding="utf-8") as file:
        file.write(input("Enter the line to append: ") + "\\n")

print("\\nFile contents:")
with open(filename, "r", encoding="utf-8") as file:
    print(file.read())
