all_node=set()
leafnode=set()
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
    else:
        root.left=insert(root.left,data)
    return root
def storenode(root):
    global all_node
    global leafnode
    if root==None:
        return
    all_node.add(root.data)
    if root.left==None and root.right==None:
        leafnode.add(root.data)
        return
    storenode(root.left)
    storenode(root.right)
def isdead(root):
    global all_node
    global leafnode
    if root is None:
        return False
    leafnode.add(0)
    storenode(root)
    for i in leafnode:
        if (i+1) in all_node and (i-1) in all_node:
            return True
    return False
if __name__ == '__main__':
    root = None
    root = insert(root, 8)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 11)
    root = insert(root, 4)
    if isdead(root):
        print("YES")
    else:
        print("NO")


