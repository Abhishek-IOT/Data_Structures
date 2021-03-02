"""
To check if the tree is BST or not we will just have the inorder traversal and check i and i+1 index value of array if arr[i+1]>arr[i]
Then it is binary tree else it is not
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root,queue):
    if root:
        inorder(root.left,queue)
        queue.append(root.data)
        print(root.data)
        inorder(root.right,queue)
def check(queue):
    bol=True
    for i in range(len(queue)-1):
        if queue[i+1]>queue[i]:
            bol=True
        else:
            bol=False
    return bol
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    # root.left.left.left = Node(10)
    queue=[]
    inorder(root,queue)
    if check(queue):
        print("Yes it is BST")
    else:
        print("No it is not")
