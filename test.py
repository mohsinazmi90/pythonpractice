def main():
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    print(weekdays[0])
    
    numbers = {1, 2, 5, 7, 1}
    print(numbers)

    
    

    students = {
        1: {"Name": "Mohsin", "Roll": 1, "Marks": 90},
        2: {"Name": "Sara", "Roll": 2,  "Marks": 80},
        3: {"Name": "Zara", "Roll": 3, "Marks": 92},
        4: {"Name": "Zaed", "Roll": 4, "Marks": 96},
    }
    for roll, student in students.items():
	    print(f"Student name: {student['Name']}, Roll number: {student['Roll']} and received grade: {student['Marks']}")


if __name__ == "__main__":
    main()