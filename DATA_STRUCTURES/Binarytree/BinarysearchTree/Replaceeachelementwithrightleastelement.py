class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    global succ
    if root is None:
        return Node(data)
    if root.data<data:
        root.right=insert(root.right,data)
    if root.data>data:
        succ=root
        root.left=insert(root.left,data)
    return root
def replace(arr,n):
    global succ
    root=None
    for i in range(n-1,-1,-1):
        succ=None
        root=insert(root,arr[i])
        if (succ):
            arr[i]=succ.data
        else:
            arr[i]=-1
    return arr


if __name__ == '__main__':
    arr = [8, 58, 71, 18, 31, 32, 63,
           92, 43, 3, 91, 93, 25, 80, 28]
    n = len(arr)
    succ = None
    arr = replace(arr, n)
    print(arr)