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

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    arr=[]
    inorder(root,arr)
    print(arr)
    for k in range(len(arr)):
        print(arr[k],k+1,"th smallest element in the array")
