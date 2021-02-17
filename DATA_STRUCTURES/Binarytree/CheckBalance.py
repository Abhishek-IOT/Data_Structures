class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1
def isbalance(root):
    if root is None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if abs(lh-rh)<=1 and isbalance(root.left) is True and isbalance(root.right) is True:
        return True
    return False
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(7)
    if(isbalance(root)):
        print("Yes")
    else:
        print("NO")
