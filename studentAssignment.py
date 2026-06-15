# Funtion to add student details to the students dictionary, 
# with input validation for unique roll numbers.
def add_student(students):
    
    # Loop to continuously add student details until the user decides to exit.
    while True:
        name = input("Enter student name: ")
        roll = int(input("Enter student roll number: "))
        
        # Check if the entered roll number already exists in the students dictionary. 
        # If it does, prompt the user to enter a unique roll number and continue the loop.
        if roll in students:
            print("Roll number already exists. Please enter a unique roll number.")
            continue
        
        # Input validation for marks to ensure they are numeric values. 
        # If the user enters invalid input, an error message is displayed and the loop continues to 
        # prompt for valid input.
        math = float(input("Enter student marks in Math: "))
        science = float(input("Enter student marks in Science: "))
        english = float(input("Enter student marks in English: "))

        # If all inputs are valid, the student details are added to the students dictionary 
        # with the roll number as the key and a nested dictionary containing the student's name 
        # and marks as the value.
        students[roll] = {
            "Name": name,
            "Roll": roll,
            "Math": math,
            "Science": science,
            "English": english,
        }

        print(f"Student with roll number {roll}, {name} added successfully!")
        
        # After adding a student, the user is prompted to decide whether to continue adding 
        # more students or exit the loop.
        cont = input("Press x to exit or any other key to continue: ").lower()
        if cont == "x":
            break

# Function to search for a student in the students dictionary based on their roll number.
def search_student(students):
    
    # Prompt the user to enter a roll number to search for. 
    # If the roll number does not exist in the students dictionary, an error message is displayed 
    # and the function returns None.
    roll_num = int(input("Enter your roll number: "))
    if roll_num not in students:
        print("Student not found!")
        return None

    # If the roll number exists, the student's details are formatted into a string and 
    # printed to the console.
    student = f"Name: {students[roll_num]['Name']} | Roll: {students[roll_num]['Roll']} | Math: {students[roll_num]['Math']} | Science: {students[roll_num]['Science']} | English: {students[roll_num]['English']}"
    print(student)


# Function to update a student's details in the students dictionary based on their roll number.
def update_student(students):
    
    # Prompt the user to enter a roll number to update. If the roll number does not exist in the 
    # students dictionary, an error message is displayed and the function returns None.
    roll_num = int(input("Enter your roll number: "))
    if roll_num not in students:
        print("Student not found!")
        return None

    # Input validation for updated marks to ensure they are numeric values. 
    # If the user enters invalid input, an error message is displayed and the function returns None.
    try:
        print(f"Enter new details for student, {students[roll_num]['Name']}:")
        name = str(input("Enter your name: "))
        math = float(input("Enter updated marks in Math: "))
        science = float(input("Enter updated marks in Science: "))
        english = float(input("Enter updated marks in English: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")
        return None
    
    # If all inputs are valid, the student's details in the students dictionary are updated 
    # with the new values.
    students[roll_num] = {
        "Name": name,
        "Roll": students[roll_num]['Roll'],
        "Math": math,
        "Science": science,
        "English": english,
    }

    # After successfully updating the student's details, a confirmation message is printed to the 
    # console.
    print(f"Student with roll number {roll_num}, {students[roll_num]['Name']} updated successfully!")


# Function to delete a student's details from the students dictionary based on their roll number.
def delete_student(students):
    
    print("Select from list below to delete student:")
    
    # Loop through the students dictionary and print the name and roll number of each student to the 
    # console, allowing the user to see the available students before selecting one to delete.
    for roll, student in students.items():
        print(f"Name: {student['Name']} | Roll: {roll}")
    
    # Prompt the user to enter a roll number to delete. If the roll number does not exist 
    # in the students dictionary, an error message is displayed and the function returns None.
    roll_num = int(input("Enter the roll number of the student you want to delete: "))
    if roll_num not in students:
        print("Student not found!")
        return None

    # If the roll number exists, the student's details are deleted from the students dictionary 
    # using the del statement.
    print(f"Student with roll number {roll_num}, {students[roll_num]['Name']} deleted successfully!")
    del students[roll_num]
    

# Function to display the details of all students in the students dictionary.
def show_all_students(students):
    
    # Loop through the students dictionary and print the name, roll number, and marks in Math, 
    # Science, and English for each student to the console.
    for roll, student in students.items():
        print(
            f"Name: {student['Name']} | Roll: {student['Roll']} | Math: {student['Math']} | Science: {student['Science']} | English: {student['English']}"
        )

# Function to calculate and display the topper (student with the highest total marks) from the 
# students dictionary.
def show_topper(students):
    
    # If the students dictionary is empty, a message is printed to the console indicating that 
    # there are no students available.
    if not students:
        print("No students available.")
        return

    # Initialize variables to keep track of the topper's name, roll number, and maximum marks.
    topper = None
    topper_roll = None
    max_marks = -1

    # Loop through the students dictionary to calculate the total marks for each student by summing 
    # their marks in Math, Science, and English. If a student's total marks are greater than the 
    # current maximum marks, the topper's name, roll number, and maximum marks are updated accordingly
    for roll, student in students.items():
        # Calculates total marks
        total_marks = student["Math"] + student["Science"] + student["English"]
        
        # If the total marks of the current student are greater than the maximum marks found so far,
        # update the topper's name, roll number, and maximum marks.
        if total_marks > max_marks:
            max_marks = total_marks
            topper = student["Name"]
            topper_roll = roll

    # Calculate the percentage of the topper's total marks out of a maximum possible score of 300 
    # (100 marks for each subject) and print the topper's details to the console.
    percentage = (max_marks / 300) * 100
    
    # Print the topper's name, roll number, and percentage in Math, Science, and English to the console
    print(
        f"{topper} (Roll {topper_roll}) is the topper with {percentage:.2f}% in Math, Science, and English."
    )

# Function to calculate and display the average marks across all students in the students dictionary.
def show_average_marks(students):
    
    # Initialize variables to keep track of the total marks and average marks. 
    # If the students dictionary is empty, a message is printed to the console indicating that 
    # there are no students available.
    total_marks = 0
    average_marks = 0
    if not students:
        print("No students available.")
        return None
    
    # Loop through the students dictionary to calculate the total marks for all students by summing 
    # their marks in Math, Science, and English. The average marks are calculated by dividing the 
    # total marks by the number of students. 
    for roll, student in students.items():
        total_marks += student["Math"] + student["Science"] + student["English"]
        average_marks = total_marks / len(students)
    
    # Calculate the percentage of the average marks out of a maximum possible score of 300 
    # (100 marks for each subject) and print the average marks to the console.
    percentage = (average_marks / 300) * 100
    
    # Print the average marks across all students as a percentage to the console, formatted 
    # to two decimal places.
    print(f"Average marks across all students: {percentage:.2f}%")

# Function to calculate and display the grades for each student in the students dictionary based on
# their marks in Math, Science, and English.
def grades(students):
    
    # Loop through the students dictionary to calculate the grade for each student based on their 
    # marks in Math, Science, and English. The grading system is as follows:
    for roll, student in students.items():
        name = student["Name"]
        math_marks = student["Math"]
        science_marks = student["Science"]
        english_marks = student["English"]

        # The grading system is as follows:
        if math_marks >= 80:
            math_grade = "A"
        elif 71 <= math_marks <= 79:
            math_grade = "B"
        elif 60 <= math_marks <= 69:
            math_grade = "C"
        else:
            math_grade = "F"

        if science_marks >= 80:
            science_grade = "A"
        elif 71 <= science_marks <= 79:
            science_grade = "B"
        elif 60 <= science_marks <= 69:
            science_grade = "C"
        else:
            science_grade = "F"

        if english_marks >= 80:
            english_grade = "A"
        elif 71 <= english_marks <= 79:
            english_grade = "B"
        elif 60 <= english_marks <= 69:
            english_grade = "C"
        else:
            english_grade = "F"

        # After calculating the grades for each subject, the student's name, roll number, and
        # grades in Math, Science, and English are printed to the console.
        print(
            f"{name} (Roll {roll}) got grade: {math_grade} in Math, got grade: {science_grade} in Science, got grade: {english_grade} in English"
        )


def main():
    # Initial student database stored as a dictionary
    students = {
        1: {"Name": "Mohsin", "Roll": 1, "Math": 85, "Science": 90, "English": 88},
        2: {"Name": "Sara", "Roll": 2, "Math": 78, "Science": 82, "English": 80},
        3: {"Name": "Atia", "Roll": 3, "Math": 92, "Science": 88, "English": 95},
        4: {"Name": "Ali", "Roll": 4, "Math": 65, "Science": 70, "English": 72},
        5: {"Name": "Zara", "Roll": 5, "Math": 55, "Science": 60, "English": 58},
        6: {"Name": "Zaed", "Roll": 6, "Math": 80, "Science": 85, "English": 82},
        7: {"Name": "Paxton", "Roll": 7, "Math": 90, "Science": 92, "English": 94},
        8: {"Name": "Aliza", "Roll": 8, "Math": 70, "Science": 75, "English": 78},
        9: {"Name": "Linda", "Roll": 9, "Math": 60, "Science": 65, "English": 68},
        10: {"Name": "Imran", "Roll": 10, "Math": 82, "Science": 88, "English": 85},
    }
    
    # Infinite loop to keep showing the menu until user chooses Exit
    while True:
        print("1. Add Student")
        print("2. Search Student")
        print("3. ⁠Update Student")
        print("4. Delete Student")
        print("5. Show All Students")
        print("6. Show Topper")
        print("7. Show Average Marks")
        print("8. Exit")

        try:
            # User selects an option from the menu
            choice = int(input("Select an option: "))
        except ValueError:
            # Handles non‑numeric input
            print("Invalid input. Please enter a number.")
            continue

        value = choice  # Just storing the choice in another variable

        # match-case works like a switch statement
        match value:
            case 1:
                add_student(students)          # Add a new student
            case 2:
                search_student(students)       # Search for a student by roll number
            case 3:
                update_student(students)       # Update marks or name
            case 4:
                delete_student(students)       # Delete a student
            case 5:
                show_all_students(students)    # Display all students
            case 6:
                show_topper(students)          # Show the highest scoring student
            case 7:
                show_average_marks(students)   # Show class average
            case 8:
                print("Exiting the program...")
                break


if __name__ == "__main__":
    main()
