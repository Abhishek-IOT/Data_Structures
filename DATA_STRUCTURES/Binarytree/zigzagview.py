"""
In this when we will be on even level we will traverse and print from left to right
and when we will be on level odd level we will traverse and print from right to left.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    if lh>rh:
        return lh+1
    else:
        return rh+1
def zigzagview(root):
    h=height(root)
    for i in range(1,h+1):
        if i%2==0:
            zigzagviewright(root,i)
        else:
            zigzagviewleft(root,i)


def zigzagviewleft(root,level):
    if root is None:
        return
    if level==1:
        print(root.data,end=" ")
    if level>1:
        zigzagviewleft(root.left,level-1)
        zigzagviewleft(root.right,level-1)

def zigzagviewright(root,level):
    if root is None:
        return
    if level==1:
        print(root.data,end=" ")
    if level>1:
        zigzagviewright(root.right,level-1)
        zigzagviewright(root.left,level-1)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    zigzagview(root)

