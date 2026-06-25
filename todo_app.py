# Open a blank file named todo_app.py and follow these instructions:
# Create a main() function.
# Check if a file named todos.json exists using os.path.exists().
# If it does: Load it into a variable named todo_list (Hint: it will be a Python list []).
# If it doesn't: Initialize todo_list = [] as an empty list.
# Ask the user for a new task: new_task = input("Enter a task: ").
# Use .append(new_task) to add it to your todo_list.
# Open todos.json in "w" mode and use json.dump(todo_list, file) to save it.

import json
import os


def main():
    if os.path.exists("todos.json"):
        with open("todos.json", "r") as file:
            todo_list = json.load(file)
            print(f"Here are the items in your to-do list: {todo_list}")
    else:
        print("File not found. Creating new task list...")
        todo_list = []

    add = "1"

    while add == "1":

        add = input("Type 1 to add a tasks, else press any key to exit: ")
        if add != "1":
            break

        task = input("Enter task: ")

        if task in todo_list:
            print("Task already exists in the list...")
            continue

        todo_list.append(task)
        print(f"Here is your updated task list: {todo_list}")

    with open("todos.json", "w") as file:
        json.dump(todo_list, file, indent=4)

    delete = "1"

    while delete == "1":
        if not todo_list:
            print("There are no tasks in your list")
            break

        delete = input("Type 1 to delete a tasks, else press any key to exit: ")
        if delete != "1":
            break

        print(f"Choose task to delete: {todo_list}")
        del_task = input("Enter task: ")

        if del_task in todo_list:
            todo_list.remove(del_task)
            print(f"Here is your updated task list: {todo_list}")
        else:
            print("Pick a task that is in your list...")

    with open("todos.json", "w") as file:
        json.dump(todo_list, file, indent=4)

    print(f"Final To-Do list: {todo_list}")


if __name__ == "__main__":
    main()
