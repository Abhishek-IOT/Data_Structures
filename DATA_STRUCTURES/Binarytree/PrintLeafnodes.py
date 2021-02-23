"""
Program to print the leaf nodes of the tree. We will have the root and then we will check that the root is not non we will go to it's left then we will
check that at present node the node.left and node.right is None.If None then we will print the data
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def leafnodes(root):
    if root:
        leafnodes(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        leafnodes(root.right)
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    leafnodes(root)