"""
First make the inorder traversal of the tree and add it in array and then make a
DLL and then add the data at the end of DLL.
"""


class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addatend(self,data):
        newNode=LinkedListNode(data)
        if self.head is None:
            self.head=newNode
            self.head.prev=None
            return
        newNode.next=None
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=newNode
        newNode.prev=temp

    def PrintList(self):
        if self.head is None:
            return
        temp = self.head
        while (temp):
            print(temp.data, end="<=>")
            temp = temp.next
        print("Null")
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root,queue):
    if root is None:
        return

    inorder(root.left,queue)
    queue.append(root.data)
    print(root.data,end=" ")
    inorder(root.right,queue)
    return queue

if __name__ == '__main__':
    root=Node(10)
    root.left=Node(12)
    root.right=Node(15)
    root.left.left=Node(25)
    root.left.right=Node(30)
    root.right.left=Node(36)
    q=[]
    m=inorder(root,q)
    print("\n")
    print(q)
    l=LinkedList()
    for i in range(len(q)):
        l.addatend(q[i])
    l.PrintList()
