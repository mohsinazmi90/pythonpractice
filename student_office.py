class Employee:
    """
    Creating employee class
    """

    def __init__(self, emp_id: int, emp_name: str, role: str, salary: float):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.role = role
        self.salary = salary
        self.performance_score = 5.0

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Successfully processed {self.emp_name}'s salary to {self.salary}.")
            return True
        print("Invalid amount. No changes made.")
        return False

    def update_performance(self, score):
        if score >= 0 and score <= 10:
            self.performance_score = score
            print(f"Updated {self.emp_name}'s score to {self.performance_score}")
            return True
        print("Invalid score. No changes made.")
        return False


class Office:
    """
    Manages data for all employees
    """

    def __init__(self, office_name: str):
        self.office_name = office_name
        self.employees = {}

    def hire_employee(self, employee):
        if employee.emp_id not in self.employees:
            self.employees[employee.emp_id] = employee
            print(f"Hired: {employee.emp_name} as {employee.role}")
        else:
            print(f"Employee {employee.emp_id} already exists!")

    def calculate_monthly_pay(self):
        total_annual_salary = sum(emp.salary for emp in self.employees.values())
        return round(total_annual_salary / 12, 2)

    def display_roster(self):
        print(f"\n------ {self.office_name} Staff ------")

        if not self.employees:
            print("No Employees Currently Hired")
            return

        for emp in self.employees.values():
            print(
                f"ID: {emp.emp_id}, Name: {emp.emp_name}, Role: {emp.role}, Salary: ${emp.salary}, Rating: {emp.performance_score}/10"
            )


tech_hub = Office("Silicone Office - San Jose")

emp1 = Employee("E101", "Steve Jobs", "CEO", 1100000)
emp2 = Employee("E102", "Steve Wozniak", "CTO", 1200000)

tech_hub.hire_employee(emp1)
tech_hub.hire_employee(emp2)
emp1.give_raise(20000)
emp2.update_performance(9.5)
tech_hub.display_roster()
