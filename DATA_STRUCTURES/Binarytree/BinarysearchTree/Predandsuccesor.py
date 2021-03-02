class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        return Node(data)
    elif root.data<data:
        root.right=insert(root.right,data)
    elif root.data>data:
        root.left=insert(root.left,data)
    return root
def inorder(root,queue):
    if root:
        inorder(root.left,queue)
        queue.append(root.data)
        print(root.data,end=" ")
        inorder(root.right,queue)
def predandsuc(queue,key):
    for i in range(len(queue)):
        if key==queue[i]:
            return i-1,i+1
    l=[]
    for i in range(len(queue)):
        if key<queue[i]:
            l.append(i-1)
            l.append(i)
            break
    return l
if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    queue=[]
    inorder(r,queue)
    print(queue)
    pr=predandsuc(queue,65)
    print(pr)
    print(queue[pr[0]],queue[pr[1]])