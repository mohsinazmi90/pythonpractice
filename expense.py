# Build a terminal-based program that lets you add, view, and analyze daily spending habits.

# How it should work (The Logic Flow):
# The Main Menu: A continuous loop that displays 4 options:

# Add Expense

# View All Expenses

# View Category Total

# Exit

# Add Expense: Ask the user for the name of the item (e.g., "Burrito"), the cost (e.g., 12.50),
# and the category (e.g., "Food").

# View All Expenses: Print out every item, its cost, and its category in a clean, readable format.

# View Category Total: Ask the user to type a category (like "Food"). The program must search 
# through all expenses, add up only the costs matching that category, and print the final sum.

# How to Structure Your Data
# To keep track of multiple data points for a single expense, you should store them inside a 
# list of dictionaries. It looks like this behind the scenes:

def user_options(expense):
    
    while True:
        try:
            print("\n1. Add Expense")
            print("2. View all Expense")
            print("3. View Category Total")
            print("4. Exit")
            
            user_select = int(input("Please select from menu below: "))
                       
            if user_select  == 1:
                add_expense(expense)
            elif user_select  == 2:
                view_all_expenses(expense)
            elif user_select  == 3:
                view_categ_total(expense)
            elif user_select  == 4:
                print("Exiting Program...")
                break
            else:
                print("Please select from valid options")
        except:
            print("Please enter valid input")
                    
def add_expense(expenses):
    name = input("Item name: ").capitalize()
    price = float(input("Cost: "))
    category = input("Category: ").capitalize()

    expense = {
        "Name": name,
        "Price": price,
        "Category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")
    return expense
    
    
def view_all_expenses(expenses):
    for expense in expenses:
        print(f"Item: {expense['Name']}, Cost: ${expense['Price']:.2f}, Category: {expense['Category']}")

def view_categ_total(expenses):
    totals = {}
    
    for expense in expenses:
        category = expense['Category']
        price = expense['Price']
        
        if category not in totals:
            totals[category] = 0
            
        totals[category] += price
        
    for category, total in totals.items():
        print(f"{category}: {total}")
        
def main():
    expenses = []
    user_options(expenses)

if __name__ == "__main__":
    main()