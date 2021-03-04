class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def buildTree(self,inorder,preorder,arr,n):
        self.root=preorder[0]
        self.root.left=preorder[1]
        pass
    