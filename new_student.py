# Q1 — Lists
# A list of 5 student names
# Print all names
# Add 1 new name
# Remove 1 name

def initial_student(students):
    print("You need to provide information for the first 5 students")
    
    count = 0
    
    while count < 5:
        try:
            print(f"\nYou are entering information for student no. {count + 1}")
            
            name = str(input("Please enter student name: "))
            roll = int(input("Please enter the roll number: "))
            if roll in students:
                print("Please use unique roll numbers")
                continue
            math = float(input("Please enter Math grades: "))
            science = float(input("Please enter Science grades: "))
            english = float(input("Please enter English grades: "))
        
            students[roll] = {
                "Name": name,
                "Roll": roll,
                "Math": math,
                "Science": science,
                "English": english
            }
            count += 1
        except:
            print("Please use the proper data...")
    
    for roll, student in students.items():
        print(f"Student: {student['Name']} | Roll: {student['Roll']}")   

def add_student(students):
    print("Lets add another student to the list...")
    ask = '1'
    
    while ask == '1':
        try:
            name = str(input("Please enter student name: "))
            roll = int(input("Please enter the roll number: "))
            if roll in students:
                print("Roll number already exists. Please enter a unique roll number.")
                continue
            math = float(input("Please enter Math grades: "))
            science = float(input("Please enter Science grades: "))
            english = float(input("Please enter English grades: "))
        
            students[roll] = {
                "Name": name,
                "Roll": roll,
                "Math": math,
                "Science": science,
                "English": english
            }
            print(f"Successfully added {students[roll]['Name']}")
            ask = str(input("Type 1 to add another student or any other button to exit: "))
        except:
            print("Please use the proper data...")
            

def remove_student(students):
    print("Lets remove a student to the list...")
    ask = '1'
    
    for roll, student in students.items():
        print(f"Student: {student['Name']}, Roll {roll}")
    
    while ask == '1':
        try:
            roll = int(input("Please enter the roll number: "))
            if roll not in students:
                print("Roll number doesn't exists. Please enter a roll number.")
                continue
        
            print(f"Successfully removed {students[roll]['Name']}")
            del students[roll]
            ask = str(input("Type 1 to delete another student or any other button to exit: "))
            
        except:
            print("Please use the proper data...")
    
    
def main():
    students = {}
    initial_student(students)
    
    while True:
        try:
            print("\n--- MENU ---")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Exit the program")
            
            ask = int(input("Please select from list above: "))
            
            match ask:
                case 1:
                    add_student(students)
                case 2:
                    remove_student(students)
                case 3:
                    print("Exiting the program...")
                    break
        except:
            print("Please select from the list above...")
    
if __name__ == "__main__":
    main()