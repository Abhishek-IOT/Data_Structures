class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def issubtree(root1,root2):
    if root1 is None:
        return False
    if root2 is None:
        return True
    if identical(root1,root2):
        return True
    return issubtree(root1.left,root2) or issubtree(root1.right,root2)
def identical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.data==root2.data and identical(root1.left,root2.left) and identical(root1.right,root2.right)
if __name__ == '__main__':
    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)
    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)
    if issubtree(S,T):
        print("Yes it is")
    else:
        print("No it is not")
