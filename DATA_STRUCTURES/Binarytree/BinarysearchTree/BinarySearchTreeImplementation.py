class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def insert(root,key):
    if root is None:
        return Node(key)
    elif root.data<key:
        root.right=insert(root.right,key)
    else :
        root.left=insert(root.left,key)
    return root
def search(root,key):
    print(root.data)
    if root is None:
        return False
    if root.data==key:
        return True
    if root.data>key:
        if root.left:
            return search(root.left,key)
        else:
            return False
    if root.data<key:
        if root.right:
            return search(root.right,key)
        else:
            return False


if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    inorder(r)
    m=search(r,20)
    if m is True:
        print("Yes")
    else:
        print("No")
    print(m)