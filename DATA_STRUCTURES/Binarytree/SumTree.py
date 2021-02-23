class newNode:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
def sumTree(root):
    if root is None:
        return 0
    old=root.data
    root.data=sumTree(root.left)+sumTree(root.right)
    return root.data+old
def preorder(root):
    if root is None:
        return
    preorder(root.left)
    print(root.data,end=" ")
    preorder(root.right)

if __name__ == '__main__':
    root=None
    root = newNode(10)
    root.left = newNode(-2)
    root.right = newNode(6)
    root.left.left = newNode(8)
    root.left.right = newNode(-4)
    root.right.left = newNode(7)
    root.right.right = newNode(5)
    m=sumTree(root)
    preorder(root)
