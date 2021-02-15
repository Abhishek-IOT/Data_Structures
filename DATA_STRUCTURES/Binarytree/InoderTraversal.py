class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end="   ")
        self.inorder(root.right)
if __name__ == '__main__':
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.right=TreeNode(3)
    t.left.left=TreeNode(4)
    t.left.right=TreeNode(6)
    t.right.right=TreeNode(5)
    t.right.left=TreeNode(7)
    t.inorder(t)
