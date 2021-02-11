"""
Program To Find the given pair in the Doubly LinkedList.
Logic=We will use two Pointer algorithm to see that sum exist or not and check the sum is equal or less or more and shift right and left pointer accordingly
we will first make the right pointer to the last and then decrease the pointer accordingly
11<=>10<=>2<=>4<=>1<=>None
Yes Found={ 11 , 1 }
Yes Found={ 10 , 2 }
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addatBeg(self,data):
        newNode=Node(data)
        newNode.next=self.head
        if self.head!=None:
            self.head.prev=newNode
        self.head=newNode
    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="<=>")
            temp=temp.next
        print("None")

    def pairsum(self,head,sum):
        first=head
        second=head
        found=False
        while(second.next!=None):
            second=second.next

        while(first!=None and second!=None and first!=second and second.next!=first):
            if (first.data+second.data)==sum:
                print("Yes Found={",first.data,",",second.data,"}")
                found=True
                first=first.next
                second=second.prev
            else:
                if (first.data+second.data)<sum:
                    first=first.next
                else:
                    second=second.prev

        if found==False:
            print("No Pair Found")

if __name__ == '__main__':
    l=LinkedList()
    l.addatBeg(1)
    l.addatBeg(4)
    l.addatBeg(2)
    l.addatBeg(10)
    l.addatBeg(11)
    l.PrintList()
    l.pairsum(l.head,12)