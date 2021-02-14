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
        if self.head !=None:
            self.head.prev=newNode
        self.head=newNode
    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="<=>")
            temp=temp.next
        print("None")
    def countTriplets(self,head,x):
        d=dict()
        curr=head
        first=curr.next
        second=head
        count=0
        while(second.next):
            second=second.next
        temp=second
        i=0
        while(curr.next!=None):
            if (first!=second and first!=None and second!=None):

                if (curr.data+first.data+second.data==x):
                    print(curr.data, first.data, second.data, "The cond1")
                    # count=count+1

                    if [second.data,first.data] !=d:
                        d[i] = [first.data,second.data]
                        count = count + 1
                        i=i+1

                    else:
                        count=count-1
                    print(d)

                    first=first.next

                    second=second.prev


                else:

                    if (curr.data+first.data+second.data<x):
                        print("Cond2", curr.data, first.data, second.data)
                        first=first.next


                    else:
                        print("Cond3", curr.data, first.data, second.data)
                        second=second.prev
            else:
                curr=curr.next
                first=curr.next
                second=temp
        return count
if __name__ == '__main__':
    l=LinkedList()
    l.addatbeg(9)
    l.addatbeg(8)
    l.addatbeg(6)
    l.addatbeg(5)
    l.addatbeg(4)
    l.addatbeg(2)
    l.addatbeg(1)
    l.PrintList()
    m=l.countTriplets(l.head,15)
    print(m)
# m={1:[1,2]}
# if [2,1]!=m[1]:
#     m[1]=[2,1]
# print(m)