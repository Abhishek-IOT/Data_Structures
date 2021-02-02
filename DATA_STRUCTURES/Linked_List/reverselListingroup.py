class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None
    def addatbeginning(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def reversegrp(self):
        start = Node(1)
        end = Node(3)
        prev = None
        curr=start
        while(curr is not end):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        start=prev


    def printList(self):
        itr=self.head
        while(itr):
            print(itr.data,end="-->")
            itr=itr.next
if __name__ == '__main__':
    l=LinkedList()
    l.addatbeginning(6)
    l.addatbeginning(5)
    l.addatbeginning(4)
    l.addatbeginning(3)
    l.addatbeginning(2)
    l.addatbeginning(1)
    l.addatbeginning(0)
    l.printList()

    l.reversegrp()
    l.printList()