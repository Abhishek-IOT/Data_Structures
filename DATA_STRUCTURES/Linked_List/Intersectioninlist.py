"""
Intersection of two sorted Linked lists
Easy Accuracy: 29.44% Submissions: 35969 Points: 2
Given two lists sorted in increasing order, create a new list representing the intersection of the two lists. The new list should be made with its own memory — the original lists should not be changed.

Example 1:

Input:
L1 = 1->2->3->4->6
L2 = 2->4->6->8
Output: 2 4 6
Explanation: For the given first two
linked list, 2, 4 and 6 are the elements
in the intersection.
Logic Make the pointer next if both were equal else increase the pointer accordingly.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addatlast(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newNode

    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")
    def intersection(self,head1,head2):
        l=[]
        temp1=head1
        temp2=head2
        while(temp1!=None and temp2!=None):
            if temp1.data==temp2.data:
                print(temp1.data)
                l.append(temp2.data)
                temp1=temp1.next
                temp2=temp2.next
            elif temp1.data>temp2.data:
                print(temp1.data,temp2.data)
                temp2=temp2.next
            else:
                print(temp2.data,temp1.data,"Last")
                temp1=temp1.next
        return l
if __name__ == '__main__':
    l=LinkedList()
    l.addatlast(1)
    l.addatlast(2)
    l.addatlast(3)
    l.addatlast(4)
    l.addatlast(6)
    l.PrintList()
    l1=LinkedList()
    l1.addatlast(2)
    l1.addatlast(4)
    l1.addatlast(6)
    l1.addatlast(8)
    l1.PrintList()
    m=l.intersection(l.head,l1.head)
    print(m)