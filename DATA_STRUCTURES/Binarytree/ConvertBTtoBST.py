class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root,arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)
def addchild(root,key):
    if root is None:
        return Node(key)
    elif key>root.data:
        root.right=addchild(root.right,key)
    elif key<root.data:
        root.left=addchild(root.left,key)
    return root

def buildTree(arr):
    root=Node(arr[0])
    for i in range(1,len(arr)):
        addchild(root,arr[i])
    return root

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)
    arr=[]
    inorder(root,arr)
    print(arr)
    arr.sort()
    root2=buildTree(arr)
    m=[]
    inorder(root2,m)
    print(m)
