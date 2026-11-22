# Practical 12: Employee class and object counting
class Employee:
    object_count = 0

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        Employee.object_count += 1

    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary:.2f}")


employees = []
count = int(input("How many employees do you want to enter? "))

for i in range(count):
    print(f"\\nEmployee {i + 1}")
    name = input("Name: ")
    employee_id = input("Employee ID: ")
    salary = float(input("Salary: "))
    employees.append(Employee(name, employee_id, salary))

print("\\nEmployee details")
for employee in employees:
    employee.display()
    print()

print("Total Employee objects created:", Employee.object_count)
