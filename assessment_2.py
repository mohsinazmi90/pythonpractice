# 13. Write a Python function named `square()` that returns the square of a number.
def square(x):
    return x * x


def main():
    # 11. Write Python code to create a variable named `student_name` and store your name in it
    student = "Mohsin"

    # 12. Create a list containing five fruits.
    fruits = ["Apple", "Banana", "Cherry", "Durian", "Pear"]

    print(square(5))

    # 14. What is the difference between a **List** and a **Tuple**? Write one point.
    print(
        "A list is a collection of objects that can be changed. Tuple is a collection of objects that is immutable, therefore cannot be changed"
    )

    # 15. Name any two tree traversal methods.
    print("1. In-order Traversal\n2. Pre-order Traversal")

    # 16.   Write a Python program that: Creates a list of five numbers.
    #       Prints the largest number in the list.
    list_of_num = [5, 102, 14, -9, 82]
    print(f"Max number is {max(list_of_num)}")

    # 17. Answer the following:
    # a) What is a Linked List? (2 Marks)
    print(
        "A linked list is a data structure that treats objects like nodes and a link to connect the objects"
    )

    # 17. b) Draw the following linked list: 10 → 20 → 30 → None
    print("(10) -> Next, (20) -> Next, (30) -> Next, None")
    print("node1 = Node(10)\nnode2 = Node(20)\nnode3 = Node(30)\n")

    print("node1.next = node2\nnode2.next = node3\nnode3.next is already None")

    # 17. c) Name any two advanced data structures (1 Mark)
    print("1. Binary Tree\n2. Linked List")


if __name__ == "__main__":
    main()
