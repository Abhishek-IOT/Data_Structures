class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def reverseList(self):
        prev=None
        curr=self.head
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    def addatbeg(self,data):
        Node1=Node(data)
        Node1.next=self.head
        self.head=Node1
    def printList(self):
        itr=self.head
        while(itr):
            print(itr.data,end="-->")
            itr=itr.next
if __name__ == '__main__':
    l=LinkedList()
    l.addatbeg(1)
    l.addatbeg(2)
    l.addatbeg(3)
    l.printList()
    l.reverseList()
    print()
    l.printList()