"""
Problem=Remove the duplicate from unsorted LinkedList.We will make the LinkedList as sorted by using the merge sort and
then we will remove the duplicates as by looking the next data element and checking the element is same or not
"""

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
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
        print('Null')
    def getmiddle(self):
        slow=self.head
        fast=self.head
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
    def Mergethesorted(self,left,right):
        if left==None:
            return right
        if right==None:
            return left
        res=None
        if left.data<right.data:
            res=left
            res.next=self.Mergethesorted(left.next,right)
        else:
            res=right
            res.next=self.Mergethesorted(left,right.next)
    def Mergesort(self,head):
        if head==None:
            return head
        mid=self.getmiddle()
        midnxt=mid.next
        mid.next=None
        left=self.Mergesort(head)
        right=self.Mergesort(midnxt)
        sortedList=self.Mergethesorted(left,right)
        return sortedList
    def deletedup(self):
        temp=self.head
        while(temp!=None and temp.next!=None):
            if temp.data==temp.next.data:
                temp.next=temp.next.next
            else:
                temp=temp.next

if __name__ == '__main__':
    l=LinkedList()
    l.addatbeg(10)
    l.addatbeg(1)
    l.addatbeg(1)
    l.addatbeg(1)
    l.addatbeg(1)
    l.addatbeg(20)
    l.addatbeg(20)
    l.addatbeg(20)
    l.addatbeg(5)
    l.addatbeg(80)
    l.addatbeg(80)
    l.addatbeg(80)
    l.addatbeg(80)
    l.addatbeg(54)
    l.printList()
    l.deletedup()
    l.printList()