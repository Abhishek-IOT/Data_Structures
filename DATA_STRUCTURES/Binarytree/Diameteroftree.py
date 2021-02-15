class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def height(self,node):
        if node is None:
            return 0
        return 1+max(self.height(node.left),self.height(node.right))
    def diameter(self,root):
        if root is None:
            return 0
        lh=self.height(root.left)
        rh=self.height(root.right)
        ldia=self.diameter(root.left)
        rdia=self.diameter(root.right)
        return max(lh+rh+1,max(ldia,rdia))
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    dia=root.diameter(root)
    print(dia)