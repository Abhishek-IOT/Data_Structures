class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addatbeg(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def reverslist(self,head):
        l=LinkedList()
        prev=None
        next=head
        curr=head
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            l.addatbeg(prev.data)
            curr=next
        return l
    def PrintL(self):
        temp=self.head
        c=0
        while(temp):
            c+=1
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")
        return c

    def chechpalin(self, head1, head2):
        temp = head1
        temp2 = head2
        c=0
        while (temp and temp2):
            print(temp.data,temp2.data)
            if temp.data == temp2.data:
                c += 1
                print(c,"djkjsdkjsdjdj")
                temp=temp.next
                temp2=temp2.next
                print(temp.data)
            else:
                print("pqpqpqpqpqp")
                break

        return c
if __name__ == '__main__':

    l=LinkedList()
    l.addatbeg(1)
    l.addatbeg(2)
    l.addatbeg(1)
    # l.addatbeg(1)
    m=l.PrintL()
    print(m,"The Lenght of List")
    t=l.reverslist(l.head)
    t.PrintL()
    tot=l.chechpalin(l.head,t.head)
    print(tot)






