from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, employee_name: str, employee_id: int):
        self.name = employee_name
        self.id = employee_id
        self._salary = 0.0
        self.__bank_account = "Not Set"

    def get_bank_account(self):
        return self.__bank_account

    def set_bank_account(self, account_number):
        if len(account_number) >= 8:
            self.__bank_account = account_number
        else:
            print("Invalid Bank Account Number Provided!")

    def display_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Account: {self.__bank_account}")

    @abstractmethod
    def calculate_pay(self) -> float:
        pass


class FullTimeEmployee(Employee):
    def __init__(self, employee_name: str, employee_id: int, monthly_salary: float):
        super().__init__(employee_name, employee_id)
        self._salary = monthly_salary

    def calculate_pay(self) -> float:
        return self._salary


class PartTimeEmployee(Employee):
    def __init__(
        self,
        employee_name: str,
        employee_id: int,
        hourly_rate: float,
        hours_worked: float,
    ):
        super().__init__(employee_name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self) -> float:
        return self.hourly_rate * self.hours_worked


class Manager:
    def __init__(self, manager_name: str):
        self.name = manager_name
        self.team = []

    def set_team(self, employee: Employee):
        self.team.append(employee)

    def display_team(self):
        name = [employee.name for employee in self.team]
        print(f'{self.name}\'s team has the following employees: [{", ".join(name)}]')


# ---- Execution of Code ----
if __name__ == "__main__":
    emp1 = FullTimeEmployee("Alice Smith", 102, 5000.00)
    emp2 = PartTimeEmployee("Bob Iger", 102, 35.00, 82.02)

    emp1.set_bank_account("US1234567")
    emp2.set_bank_account("UK7654321")

    employees = [emp1, emp2]

    for employee in employees:
        employee.display_details()
        print(f"Calculated Pay: ${employee.calculate_pay():.2f}")
        print("-" * 30)

    ron = Manager("Ron")
    ron.set_team(emp1)
    ron.set_team(emp2)

    ron.display_team()

# from abc import ABC, abstractmethod


# class Employee(ABC):
#     def __init__(self, employee_name: str, employee_id: int):
#         self.name = employee_name
#         self.id = employee_id

#         # Encapsulation
#         self._salary = 0.0
#         self.__bankaccount = "Not Set"

#     # Abstract method for the salary
#     @abstractmethod
#     def calculate_pay(self) -> float:
#         pass

#     # Define getter to display bank account number
#     def get_bank_account(self):
#         return self.__bankaccount

#     # Define setter to set bank account number
#     def set_bank_account(self, account_number: str):
#         if len(account_number) >= 8:
#             self.__bankaccount = account_number
#         else:
#             print("Invalid Bank Account Number!")

#     def display_details(self):
#         print(f"ID: {self.id}, Name: {self.name}, Account: {self.__bankaccount}")


# class FullTimeEmployee(Employee):
#     def __init__(self, employee_name: str, employee_id: int, monthly_salary: float):
#         super().__init__(employee_name, employee_id)
#         self._salary = monthly_salary

#     # Polymorphism
#     def calculate_pay(self) -> float:
#         return self._salary


# class PartTimeEmployee(Employee):
#     def __init__(
#         self,
#         employee_name: str,
#         employee_id: int,
#         hourly_rate: float,
#         hours_worked: float,
#     ):
#         super().__init__(employee_name, employee_id)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_pay(self) -> float:
#         return self.hourly_rate * self.hours_worked


# class Manager:
#     def __init__(self, manager_name: str):
#         self.name = manager_name
#         self.team = []

#     def set_manager(self, employee: Employee):
#         self.team.append(employee)

#     def display_team(self) -> str:
#         name = [employee.name for employee in self.team]
#         return f"{self.name}'s team includes the following: {', '.join(name)}"


# # ----Execution of Code----
# if __name__ == "__main__":
#     print("Creating Employees")

#     # Create Employee
#     emp1 = FullTimeEmployee("Alice", 100, 5000.00)
#     emp2 = PartTimeEmployee("Bob", 102, 35.0, 80)

#     # Set Emp Bank Account
#     emp1.set_bank_account("123456789")
#     emp2.set_bank_account("987654321")

#     employees = [emp1, emp2]

#     # Set Manager
#     ron = Manager("Ronald")
#     ron.set_manager(emp1)
#     ron.set_manager(emp2)

#     # Print Employee Info
#     for employee in employees:
#         employee.display_details()
#         print(f"Calculated Pay: ${employee.calculate_pay():.2f}")
#         print("-" * 30)

#     print(ron.display_team())
