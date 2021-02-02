"""
Remove duplicate element from sorted Linked List
Easy Accuracy: 46.37% Submissions: 71657 Points: 2
Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.

Example 1:

Input:
LinkedList: 2->2->4->5
Output: 2 4 5
Explanation: In the given linked list
2 ->2 -> 4-> 5, only 2 occurs more
than 1 time.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addatbeg(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def printLink(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="=>")
            temp=temp.next
        print("None")
    def deleteduplicate(self):
        temp=self.head
        while(temp!=None and temp.next!=None):
            if temp.data==temp.next.data:
                temp.next=temp.next.next
            else:
                temp=temp.next
if __name__ == '__main__':
    l=LinkedList()
    l.addatbeg(1)
    l.addatbeg(2)
    l.addatbeg(2)
    l.addatbeg(2)
    l.addatbeg(2)
    l.addatbeg(3)
    l.addatbeg(4)
    l.addatbeg(5)
    l.addatbeg(5)
    l.addatbeg(5)
    l.printLink()
    l.deleteduplicate()
    l.printLink()