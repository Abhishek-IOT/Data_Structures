class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        return Node(data)
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
def Count(l,h,arr):
    mcount=0
    lcount=0
    for i in range(len(arr)):
        if arr[i]<=l:
            mcount+=1
        if arr[i]<=h:
            lcount+=1
    return lcount-mcount+1

if __name__ == '__main__':
    root=None
    root=insert(root,10)
    root=insert(root,5)
    root=insert(root,1)
    root=insert(root,50)
    root=insert(root,40)
    root=insert(root,100)
    arr=[]
    inorder(root,arr)
    print(arr)
    l=5
    h=45
    m=Count(l,h,arr)
    print(m)