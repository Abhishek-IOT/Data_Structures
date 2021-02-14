"""
Print the root then it's child.
Logic =We will use queue for doing this....First we will take root in queue and then it's left and rigt and print data
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def PrintTree(self,root):
        if root is None:
            return 'N'
        q=[]
        q.append(root)
        while(len(q)>0):
            print(q[0].data,end=" ")

            node=q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

if __name__ == '__main__':
    t=Node(1)
    t.left=Node(2)
    t.right=Node(3)
    # t.PrintTree(t)
    t.left.left=Node(10)
    t.right.right=Node(9)
    t.PrintTree(t)