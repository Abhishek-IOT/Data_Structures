class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,key):
    if root==None:
        return Node(key)
    if root.data==key:
        return Node(key)
    if root.data<key:
        root.right=insert(root.right,key)
    elif root.data>key:
        root.left=insert(root.left,key)
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
    reve=arr[::-1]
    k=1
    print(reve[k-1])
    print(arr)