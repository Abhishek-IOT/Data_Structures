"""
We can know what are the no of swaps by converting the tree to
inoder and then as comparing the inoder of binary tree and binary search tree
(inorder of binary search tree is sorted) so we will just apply the algorithm to
find the minimum no of swaps to make a array as sorted.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root,queue):
    if root is None:
        return
    inorder(root.left,queue)
    print(root.data,end=" ")
    queue.append(root.data)
    inorder(root.right,queue)
    return queue
def minimumswaps(arr,n):
    ans=0
    temp=arr.copy()
    temp.sort()
    for i in range(n):
        if arr[i]!=temp[i]:
            ans+=1
            swap(arr,i,index(arr,temp[i]))
    return ans
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def index(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
    return -1

if __name__ == '__main__':
    q=[]
    root=Node(3)
    root.left=Node(2)
    root.right=Node(1)
    inorder(root,q)
    m=minimumswaps(q,len(q))
    print()
    print(m)