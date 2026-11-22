# Practical 15: Exception handling for a name
try:
    name = input("Enter your name: ").strip()

    if not name:
        raise ValueError("Name cannot be empty.")
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name should contain only letters and spaces.")

    print("Hello,", name)
except ValueError as error:
    print("Invalid name:", error)
finally:
    print("Program execution completed.")
