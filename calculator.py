def addition(a, b):
    sum = a + b
    return sum


def subtract(a, b):
    return a - b


def multiple(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ZeroDivisionError


def calculator():
    while True:
        try:
            print("\n1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            choice = int(input("Select from the following: "))
            # print(type(choice))

            if choice == 5:
                print("Exiting Program...")
                break

            if choice not in [1, 2, 3, 4]:
                print("Please make correct choice from the list..")
                continue

            num1 = int(input("Enter number: "))
            num2 = int(input("Enter second number: "))

            match choice:
                case 1:
                    print(f"Addition of {num1} and {num2} is: {addition(num1, num2)}")
                case 2:
                    print(
                        f"Subtraction of {num1} and {num2} is: {subtract(num1, num2)}"
                    )
                case 3:
                    print(
                        f"Multiplication of {num1} and {num2} is: {multiple(num1, num2)}"
                    )
                case 4:
                    print(
                        f"Division of {num1} and {num2} is: {float(divide(num1, num2))}"
                    )
        except:
            print("Please select correct option and enter valid numbers.")


def main():
    calculator()


if __name__ == "__main__":
    main()
