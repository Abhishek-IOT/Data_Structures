"""
Add 1 to a number represented as linked list
Easy Accuracy: 51.33% Submissions: 27858 Points: 2
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Example 1:

Input:
LinkedList: 4->5->6
Output: 457
Logic=First We will reverse the LinkedList and then we will add 1 and then check that if we are getting carry
If we are getting carry then we will update the next list.data accordingly and at last we will reverse the linkedList.
"""
class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None
    def addAtBeg(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def reverseList(self,head):
        temp=head
        prev=None
        curr=head
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        return self.head
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")
    def addOne(self,head):
        head=self.reverseList(head)
        k=head
        carry=0
        prev=None
        head.data+=1
        while(head!=None) and (head.data>9 or carry>0):
            prev=head
            head.data+=carry
            carry=head.data//10
            head.data=head.data%10
            head=head.next
        if carry>0:
            prev.next=Node(carry)
        return self.reverseList(k)
if __name__ == '__main__':
    l=LinkedList()
    # l.addAtBeg(1)
    l.addAtBeg(9)
    l.addAtBeg(9)
    l.addAtBeg(9)
    l.addAtBeg(1)
    l.printList()
    l.addOne(l.head)
    l.printList()

