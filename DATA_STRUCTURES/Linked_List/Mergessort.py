"""
Merge Sort in Linked List
First We will divide the Linked List into 2 parts(left and right) and the then we will merge the list such that we will value in sorted order.
For Getting the Middle use to pointer fast and slow(Fast will move 2 times and slow will move 1 time so when we will have fast at last slow will be at middle.

"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def addatbegin(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def printList(self,head):
        temp=head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")

    def getmiddile(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeList(self,left ,right):
        res=None
        if left==None:
            return right
        if right==None:
            return left
        if left.data<=right.data:
            res=left
            res.next=self.mergeList(left.next,right)
        else:
            res=right
            res.next=self.mergeList(left,right.next)
        return res
    def mergesort(self,head):
        if head==None or head.next==None:
            return head
        mid=self.getmiddile(head)
        midnxt=mid.next
        mid.next=None
        left=self.mergesort(head)
        right=self.mergesort(midnxt)
        sortlist=self.mergeList(left,right)
        return sortlist

if __name__ == '__main__':
    l=LinkedList()
    l.addatbegin(1)
    l.addatbegin(10)
    l.addatbegin(20)
    l.addatbegin(12)
    l.addatbegin(0)
    l.printList(l.head)
    l.mergesort(l.head)
    l.printList(l.head)


