def add_task():
    task = input("Enter task: ")
    return task


def edit_task(tasks):
    try:
        for value, task in enumerate(tasks):
            print(f"{value + 1}: {task}")
        task_select = int(input("Which task do you want to edit? "))

        if 0 >= task_select or task_select > len(tasks):
            print("Selection is out of bounds")
        else:
            print(f"Task '{tasks[task_select - 1]}', has been updated")
            new_task = input("Enter updated task: ")
            tasks[task_select - 1] = new_task

    except ValueError:
        print("You need to select from the available tasks...")


def del_tasks(tasks):
    try:
        for value, task in enumerate(tasks):
            print(f"{value + 1}: {task}")
        task_select = int(input("Which task do you want to delete? "))

        if 0 >= task_select or task_select > len(tasks):
            print("Selection is out of bounds")
        else:
            print(f"Task '{tasks[task_select - 1]}', is deleted")
            tasks.pop(task_select - 1)

    except ValueError:
        print("You need to select from the available tasks...")


def todo():
    tasks = []
    completed = []

    while True:
        try:
            print("\n1. Add task")
            print("2. View tasks")
            print("3. Edit task")
            print("4. Mark task as completed")
            print("5. Delete task")
            print("6. Exit program")

            choice = int(input("\nPlease make a selection: "))

            if choice not in (1, 2, 3, 4, 5, 6):
                print("Please choose from list...")
                continue

            match choice:
                case 1:
                    tasks.append(add_task())
                    print("Task added")
                case 2:
                    print("Following tasks are in the to-do list...")
                    for value, task in enumerate(tasks):
                        print(f"{value + 1}: {task.title()}")
                    if completed:
                        print("Completed tasks...")
                        for value, task in enumerate(completed):
                            print(f"{value + 1}: {task.title()}")
                case 3:
                    if not tasks:
                        print("Nothing to edit...")
                        continue
                    edit_task(tasks)
                case 4:
                    try:
                        if not tasks:
                            print("There are no tasks in your to-do list...")
                            continue
                        for value, task in enumerate(tasks):
                            print(f"{value + 1}: {task}")

                        task_select = int(
                            input("Which task do you want to mark complete: ")
                        )

                        if 0 >= task_select or task_select > len(tasks):
                            print("Selection is out of bounds")
                            continue
                        else:
                            print(
                                f"Task '{tasks[task_select - 1]}', is marked completed"
                            )
                            completed.append(tasks[task_select - 1])
                            tasks.pop(task_select - 1)

                    except ValueError:
                        print("You need to select from the available tasks...")
                case 5:
                    if not tasks:
                        print("There is nothing to delete...")
                        continue
                    del_tasks(tasks)
                case 6:
                    print("Exiting program...")
                    break

        except ValueError:
            print("Please select from proper list")


def main():
    todo()


if __name__ == "__main__":
    main()
