class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        return Node(data)
    if root.data==data:
        return

    if root.data<data:
        root.right=insert(root.right,data)
    if root.data>data:
        root.left=insert(root.left,data)
    return root
def inorder(root,arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)
def countPairs(arr1,arr2,x):
    c=0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]+arr2[j]==x:
                c=c+1
    return c
if __name__ == '__main__':
    root=None
    root=insert(root,5)
    insert(root,3)
    insert(root,7)
    insert(root,2)
    insert(root,4)
    insert(root,6)
    insert(root,8)
    root1=None
    root1=insert(root1,10)
    insert(root1,6)
    insert(root1,15)
    insert(root1,3)
    insert(root1,8)
    insert(root1,11)
    insert(root1,18)
    arr1=[]
    arr2=[]
    inorder(root,arr1)
    inorder(root1,arr2)
    print(arr1)
    print(arr2)
    x=16
    m=countPairs(arr1,arr2,x)
    print(m)
