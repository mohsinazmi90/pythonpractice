# Q4. Dictionaries
# Create a dictionary to store the following student information:
# •     Name
# •     Roll Number
# •     Class
# •     Marks
# Then display all key–value pairs in the dictionary.

def main():
    
    students = {
        1: {"Name": "Mohsin", "Roll": 1, "Class": "Math", "Marks": 90},
        2: {"Name": "Sara", "Roll": 2, "Class": "Science", "Marks": 80},
        3: {"Name": "Zara", "Roll": 3, "Class": "Arts", "Marks": 92},
        4: {"Name": "Zaed", "Roll": 4, "Class": "English", "Marks": 96},
    }
    
    print(f"{'Name':<10} {'Roll':<6} {'Class':<10} {'Marks':<6}") 
    print('-' * 40)
    
    for roll, student in students.items():
        print(f"{student['Name']:<10} {roll:<6} {student['Class']:<10} {student['Marks']:<6}")
    
if __name__ == "__main__":
    main()