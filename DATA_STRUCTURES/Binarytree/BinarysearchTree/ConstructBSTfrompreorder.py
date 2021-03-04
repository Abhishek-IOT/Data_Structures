class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def insert(root,key):
    if root is None:
        return Node(key)
    elif root.data<key:
        root.left=insert(root.left,key)
    else :
        root.right=insert(root.right,key)
    return root
# def addchild(root,key):
#     if root.data==key:
#         return
#     if key<root.data:
#         if root.left:
#             addchild(root.left,key)
#         else:
#             root.left=Node(key)
#     if key>root.data:
#         if root.right:
#             addchild(root.right,key)
#         else:
#             root.right=Node(key)
def preoder(root,arr):
    if root:
        arr.append(root.data)
        print(root.data,end=" ")
        preoder(root.left,arr)
        preoder(root.right,arr)
def buildTree(arr):
    root=Node(arr[0])
    for i in range(1,len(arr)):
        insert(root,arr[i])
    return root
if __name__ == '__main__':
    arr=[1,2,4,5,3]
    r=buildTree(arr)
    m=[]
    preoder(r,m)
