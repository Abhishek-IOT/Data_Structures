from collections import deque


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def inorder(self,root):
        stack=deque()
        curr=root
        while(stack or curr):
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                print(curr.data,end=" ")
                curr=curr.right
if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(6)
    t.right.right = TreeNode(5)
    t.right.left = TreeNode(7)
    t.inorder(t)