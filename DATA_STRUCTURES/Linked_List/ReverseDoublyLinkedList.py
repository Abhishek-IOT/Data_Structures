"""
Program to reverse a Doubly LinkedList
1<=>2<=>3 to
3<=>2<=>1
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLink:
    def __init__(self):
        self.head=None
    def addatbegining(self,data):
        newNode=Node(data)
        newNode.next=self.head
        if self.head!=None:
            self.head.prev=newNode
        self.head=newNode
        newNode.prev = None
    def PrintList(self,head):
        temp=head
        while(temp):
            print(temp.data,end="<=>")
            temp=temp.next
        print("Null")
    def reversetheList(self):

        temp=None
        curr=self.head
        while(curr!=None):
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if temp is not None:
            self.head=temp.prev


if __name__ == '__main__':
    l=DoublyLink()
    l.addatbegining(1)
    l.addatbegining(2)
    l.addatbegining(3)
    l.addatbegining(4)
    l.PrintList(l.head)
    l.reversetheList()
    l.PrintList(l.head)