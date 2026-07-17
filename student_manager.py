from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    @abstractmethod
    def display_info(self):
        pass


class Student(User):
    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        major: str,
        enrolled_courses,
        tuition_balance: float,
    ):
        super().__init__(user_id, name, email)
        self.major = major
        self.enrolled_courses = enrolled_courses
        self.tuition_balance = tuition_balance

    def pay_tuition(self, amount):
        if amount > 0:
            self.tuition_balance -= amount
            print(
                f"\nRemaining tuition balance for {self.name}: ${self.tuition_balance:.2f}"
            )
            return True
        else:
            print("Invalid amount entered.")
            return False

    def enroll_in_course(self, course):
        if course not in self.enrolled_courses:
            print(f"{self.name}: enrolled in course {course}")
            self.enrolled_courses.append(course)
            return True
        else:
            print(f"{self.name} is already enrolled in {course}")
            return False

    def display_info(self):
        print(
            f"\nStudent Info:\nID: {self.user_id},\nName: {self.name},\nE-Mail: {self.email},\nMajor: {self.major},\nCourses: {self.enrolled_courses},\nTuition Balance: ${self.tuition_balance:.2f}"
        )


class Professor(User):
    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        department: str,
        salary: float,
        assigned_course,
    ):
        super().__init__(user_id, name, email)
        self.department = department
        self.salary = salary
        self.assigned_course = assigned_course

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            new_salary = f"\nIncreased salary for professor: {self.name}, to ${self.salary:.2f}".title()
            print(new_salary)
            return True
        else:
            print("Invalid amount entered.")
            return False

    def display_info(self):
        print(
            f"\nProfessor Info:\nID: {self.user_id},\nName: {self.name},\nE-Mail: {self.email},\nDepartment: {self.department},\nAssigned Courses: {self.assigned_course},\nSalary: ${self.salary:.2f}"
        )


# ======= Execute Code ========

stud1 = Student(
    "101",
    "Mohsin Azmi",
    "mohsin.azmi@yahoo.com",
    "CS",
    ["CS101", "CS102", "CS201"],
    12050.00,
)
stud2 = Student(
    "102",
    "Hasan Azmi",
    "hasan.azmi@yahoo.com",
    "Medicine",
    ["BIO101", "BIO102"],
    22050.00,
)

prof1 = Professor(
    "1001", "Sara Khan", "sara.khan@yahoo.com", "Science", 65000.00, ["CS101", "CS102"]
)

stud1.display_info()
stud1.pay_tuition(5000.00)

stud1.display_info()
prof1.display_info()

prof1.give_raise(3000.50)
prof1.display_info()
