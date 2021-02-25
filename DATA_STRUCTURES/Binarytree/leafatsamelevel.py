class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
def check(root):
    level=0
    check.leaflevel=0
    return checkutil(root,level)
def checkutil(root,level):
    if root is None:
        return True
    if root.left is None and root.right is None:
        if check.leaflevel==0:
            check.leaflevel=level
            return True
        return level==check.leaflevel
    return (checkutil(root.left,level+1)) and (checkutil(root.right,level+1))


if __name__ == '__main__':
    root = Node(12)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(9)
    root.left.left.left = Node(1)
    # root.left.right.left = Node(2)
    if check(root):
        print("Yes they are on same level")
    else:
        print("No they are not in same level")