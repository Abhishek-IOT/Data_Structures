"""
Move last element to front of a given Linked List
Difficulty Level : Basic
 Last Updated : 30 Oct, 2020
Write a function that moves the last element to the front in a given Singly Linked List. For example, if the given Linked List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4.

"""
class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
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
    # def deletlastNode(self,head):
    #     if head==None:
    #         return None
    #     if head.next==None:
    #         head=None
    #         return head
    #     temp=head
    #     while(temp.next.next!=None):
    #         temp=temp.next
    #     temp.next=None
    #     return head

    def MoveLastoFront(self):
        temp=self.head
        newNode=None
        if not temp or not temp.next:
            return
        while(temp!=None and temp.next!=None):
            newNode = temp
            temp=temp.next

        newNode.next=None
        temp.next = self.head
        self.head = temp


if __name__ == '__main__':
    l=LinkedList()
    l.addatBeg(1)
    l.addatBeg(2)
    l.addatBeg(3)
    l.addatBeg(22)
    l.addatBeg(8)
    l.PrintList()
    l.MoveLastoFront()
    l.PrintList()
