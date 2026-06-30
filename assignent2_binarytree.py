class TreeNode:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.left = None
        self.right = None


class StudentTree:
    def __init__(self):
        self.root = None

    def insert(self, name, marks):
        self.root = self._insert(self.root, name, marks)

    def _insert(self, node, name, marks):
        if node is None:
            return TreeNode(name, marks)
        if marks < node.marks:
            node.left = self._insert(node.left, name, marks)
        else:
            node.right = self._insert(node.right, name, marks)
        return node

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"{node.name} -> {node.marks}")
            self._inorder(node.right)


students_tree = StudentTree()
students_tree.insert("Ali", 85)
students_tree.insert("Sara", 92)
students_tree.insert("John", 76)
students_tree.insert("Fatima", 88)

print("\nTree:")
students_tree.inorder()
