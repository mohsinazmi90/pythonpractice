class Node:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, marks):
        new_node = Node(name, marks)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.name} -> {temp.marks}")
            temp = temp.next


students_ll = LinkedList()
students_ll.insert("Ali", 85)
students_ll.insert("Sara", 92)
students_ll.insert("John", 76)
students_ll.insert("Fatima", 88)

print("\nLinked List:")
students_ll.display()
