class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(root):
    if root==None:
        return -1
    else:
        lh=height(root.left)
        rh=height(root.right)
        if lh>rh:
            return lh+1
        else:
            return rh+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
m=height(root)
print(m)
