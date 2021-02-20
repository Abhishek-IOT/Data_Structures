class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def height(root):
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    if lh>rh:
        return lh+1
    else:
        return rh+1
def PrintGivenlevel(root,level):
    if root is None:
        return
    if level==1:
        print(root.data,end="  ")
    if level>1:
        PrintGivenlevel(root.left,level-1)
        PrintGivenlevel(root.right,level-1)

def printTree(root):
    h=height(root)
    for i in range(1,h+1):
        PrintGivenlevel(root,i)
if __name__ == '__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(53)
    root.left.right=Node(51)
    root.right.left=Node(52)
    root.left.right.right=Node(50)
    h=height(root)
    print(h)
    printTree(root)