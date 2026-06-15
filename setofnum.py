# Q3. Sets
# •     Create a set containing ten numbers, including some duplicate values.
# •     Display the set.
# •     Explain what happened to the duplicate values and why.

def main():
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2}
    
    print(numbers)
    
    print("\nExplanation:")
    print("Duplicate values were removed because sets only store unique elements.")
    print("A set automatically eliminates duplicates to ensure all items are unique.\n")

if __name__ == "__main__":
    main()