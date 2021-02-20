"""
Left View of Binary Tree
Easy Accuracy: 37.86% Submissions: 100k+ Points: 2
Given a Binary Tree, print Left view of it. Left view of a
 Binary Tree is set of nodes visible when tree is visited from
 Left side. The task is to complete the function leftView(),
 which accepts root of the tree as argument.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def rightview(root):
    maxlevel=[0]
    return rightviewutil(root,1,maxlevel)
def rightviewutil(root,level,maxlevel):
    if root is None:
        return
    if maxlevel[0]<level:
        print(root.data)
        maxlevel[0]=level

    rightviewutil(root.right,level+1,maxlevel)
    rightviewutil(root.left,level+1,maxlevel)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(53)
    root.left.right = Node(51)
    root.right.left = Node(52)
    root.left.right.right = Node(50)
    rightview(root)