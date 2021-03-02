"""
Algorithm:

Create a recursive function that takes a node and the two values n1 and n2.
If the value of the current node is less than both n1 and n2, then LCA lies in the right subtree. Call the recursive function for thr right subtree.
If the value of the current node is greater than both n1 and n2, then LCA lies in the left subtree. Call the recursive function for thr left subtree.
If both the above cases are false then return the current node as LCA.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def LCA(root,n1,n2):
    if root is None:
        return None
    if root.data>n1 and root.data>n2:
        return LCA(root.left,n1,n2)
    if root.data<n1 and root.data<n2:
        return LCA(root.right,n1,n2)
    return root
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    n1=10
    n2=22
    m=LCA(root,n1,n2)
    print(m.data)

