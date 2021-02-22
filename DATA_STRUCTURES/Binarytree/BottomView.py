class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.hd=0
def bottomview(root):
    if root is None:
        return
    queue=[]
    hd=0
    map=dict()
    queue.append(root)
    root.hd=hd
    while(len(queue)):
        root=queue[0]
        hd=root.hd
        map[hd]=root.data
        if root.left:
            root.left.hd=hd-1
            queue.append(root.left)
        if root.right:
            root.right.hd=hd+1
            queue.append(root.right)
        queue.pop(0)
    print(map)
    for i in sorted(map):
        print(map[i],end=" ")
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    bottomview(root)