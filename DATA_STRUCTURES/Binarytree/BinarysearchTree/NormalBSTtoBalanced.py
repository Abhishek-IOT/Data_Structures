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
def buildTreeutil(arr,start,end):
    if start>end:
        return None
    print(start,end)
    mid=(start+end)//2
    node=arr[mid]
    node.left=buildTreeutil(arr,start,mid)
    node.right=buildTreeutil(arr,mid+1,end)
    return arr
def buildTree(root):
    arr=[]
    inorder(root,arr)
    n=len(arr)
    return buildTreeutil(arr,0,n-1)
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)

    root2=buildTree(root)
    print(root2.data)
    preorder(root2)

    preorder(root)