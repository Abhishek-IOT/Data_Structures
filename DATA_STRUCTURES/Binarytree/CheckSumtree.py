class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sumtree(root):
    if root is None:
        return 0
    return sumtree(root.left)+root.data+sumtree(root.right)
def issumtree(root):
    if root is None or root.left is None and root.right is None:
        return 1
    left=sumtree(root.left)
    right=sumtree(root.right)
    if root.data==left+right and issumtree(root.right) and issumtree(root.left):
        return 1

if __name__ == '__main__':
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(10)
    root.left.right=Node(10)
    if sumtree(root)==True:
        print("YEs")
    else:
        print("NO")

