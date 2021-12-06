# Dailychallenge Polygons Binary Tree
# Part 1: The Binary Tree
# Let’s start by implementing a representation of a binary tree (a tree where every node has at most two children), a tree is represented by its root node.
# Create a class Node, it has three attributes, left, right and value, respectively its left and right child and its value, the children can be None.
# Then add the basic methods to this class: get_left(), get_right(), set_left(node), set_right(node), set_value(value) and get_value().

# Part 2: The Binary Search Tree
# Now let’s transform this binary tree into a binary search tree, implement a function add_node(node) and add it to the three, make sure you respect all the conditions of the binary search tree (the node needs to be added at the right place, depending on its value).

# Part 3: Use The Binary Search Tree
# Implement a method search(value) which return the node containing this value inside the tree.

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_node(self, root, node):
        if root is None:
            return node
        if root.value < node.value:  # go to right
            root.rigth = self.add_node(root.right, node)
        else:
            self.left = self.add_node(root.left, node)  # go to left

    def search(self, root, value):
        if root.value == value:
            if root.value > value:
                return self.search(root.left, value)  # go left
            else:
                return self.search(root.right, value)  # go right


root = Node(None, None, 8)
node3 = (None, None, 3)
node10 = (None, None, 10)

root.search(root, 3)


root.add_node(root, node3)
root.add_node(root, node10)
