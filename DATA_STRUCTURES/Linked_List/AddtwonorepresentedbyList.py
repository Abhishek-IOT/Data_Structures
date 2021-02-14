class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addatBeg(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")
    def addTwoNumber(self,head1,head2):
        m=LinkedList()
        temp=head1
        temp1=head2
        carry=0
        prev=None
        teemp=None
        while(head1!=None or head2!=None):
            firstdata=0 if head1 is None else head1.data
            seconddta=0 if head2 is None else head2.data
            s=carry+firstdata+seconddta
            print(s)
            carry=1 if s>=10 else 0
            s=s if s<10 else s%10
            print(s,"jdskjds")
            teemp=Node(s)
            if self.head is None:
                self.head=teemp
            else:
                prev.next=teemp
            prev=teemp
            if head2!=None:
                head2=head2.next
            if head1!=None:
                head1=head1.next
        if carry>0:
            teemp.next=Node(carry)


if __name__ == '__main__':
    l1=LinkedList()
    l1.addatBeg(5)
    l1.addatBeg(4)
    l2=LinkedList()
    l2.addatBeg(5)
    l2.addatBeg(4)
    l2.addatBeg(3)
    l1.PrintList()
    l2.PrintList()
    res=LinkedList()
    res.addTwoNumber(l1.head,l2.head)
    res.PrintList()
