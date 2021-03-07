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
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
def build(arr):
    root=Node(arr[0])
    for i in range(1,len(arr)):
        root=insert(root,arr[i])
    return root

if __name__ == '__main__':
    arr=[40,30,32,35,80,90,100,120]
    root=build(arr)
    postorder(root)

