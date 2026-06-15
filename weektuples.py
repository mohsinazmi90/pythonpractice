# Q2. Tuples
# •     Create a tuple containing the names of the seven days of the week.
# •     Display the tuple.
# •     Explain why the elements of a tuple cannot be modified.

def main():
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    
    for i, day in enumerate(week, start = 1):
        print(f"Day {i}: {day}")
    
    print("\nExplanation:")
    print("Tuple elements cannot be modified because tuples are immutable.")
    print("Immutability means that once a tuple is created, its values cannot be changed, added, or removed.")
    
if __name__ == "__main__":
    main()