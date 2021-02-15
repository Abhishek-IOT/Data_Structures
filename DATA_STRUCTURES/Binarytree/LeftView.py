"""
Left View of Binary Tree
Easy Accuracy: 37.86% Submissions: 100k+ Points: 2
Given a Binary Tree, print Left view of it. Left view of a
 Binary Tree is set of nodes visible when tree is visited from
 Left side. The task is to complete the function leftView(),
 which accepts root of the tree as argument.
"""
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def Leftview(self,root):
        if root is None:
            return
        print(root.data,end="  ")
        self.Leftview(root.left)

if __name__ == '__main__':
    t=TreeNode(10)
    t.left=TreeNode(20)
    t.left.left=TreeNode(40)
    t.right=TreeNode(30)
    t.left.right=TreeNode(60)
    t.Leftview(t)