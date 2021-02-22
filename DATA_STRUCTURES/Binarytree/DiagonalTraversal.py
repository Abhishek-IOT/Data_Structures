"""
We will make the traversal according to the slopes of the tree.
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.hd=0

def diagonal(root):
    map=dict()
    diagonalutil(root,0,map)
    for i in map:
        for j in map[i]:
            print(j,end=" ")
        print("\n")
def diagonalutil(root,d,map):
    if root is None:
        return
    try:
        map[d].append(root.data)
    except KeyError:
        map[d]=[root.data]

    diagonalutil(root.left,d+1,map)
    diagonalutil(root.right,d,map)
if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    diagonal(root)