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

def minval(root):
    if root.left is None:
        return root.data
    return minval(root.left)
def delete(root,key):
    if key>root.data:
        if root.right:
            root.right=delete(root.right,key)
    elif key<root.data:
        if root.left:
            root.left=delete(root.left,key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        val=minval(root.right)
        root.data=val
        root.right=delete(root.right,val)
    return root
def findmax(root):
    if root.right is None:
        return root.data
    return findmax(root.right)
if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    inorder(r)
    delete(r,60)
    print()
    inorder(r)
    m=findmax(r)
    print()
    print(m)