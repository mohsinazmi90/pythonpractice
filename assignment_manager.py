# Q13: Create a backend office data system demonstrating core OOP principles.
# Write a base class Employee and a child class Manager that satisfies the following criteria:

# Encapsulation: Protect the employee's salary attribute by making it private or protected.
# Provide a property getter method to access it safely.
# Inheritance & Polymorphism: Provide a method called calculate_bonus().
# In the base Employee class, the bonus is a flat 10% of the salary.
# In the Manager class, override the method to make the bonus 20% of the salary plus a flat team
# bonus constant.


# from abc import ABC, abstractmethod


class Employee:
    def __init__(self, emp_id, emp_name, salary=0.0):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self._salary = salary

    def get_salary(self):
        return f"Current Salary for {self.emp_name}: {self._salary:.2f}"

    def set_salary(self, salary):
        self._salary = salary

    def calculate_bonus(self, bonus=0.10):
        return f"Bonus would be {(self._salary * bonus):.2f}"


class Manager(Employee):
    def __init__(self, emp_id, emp_name):
        super().__init__(emp_id, emp_name)

    def calculate_bonus(self, bonus=0.20):
        return f"Bonus would be {(self._salary * bonus) + 500:.2f}"


emp1 = Employee(101, "Mohsin", 5000)
man1 = Manager("102", "Hasan")

man1.set_salary(2000)

print(emp1.get_salary())
print(man1.get_salary())
print(emp1.calculate_bonus())
print(man1.calculate_bonus())
