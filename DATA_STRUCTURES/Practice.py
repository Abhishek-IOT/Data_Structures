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
    def printList(self):
        node=self.head
        while(node!=None):
            print(node.data,end='=>')
            node=node.next
    def palindrome(self,head):
        slow=self.head
        fast=self.head
        stack=[]
        while(fast!=None and fast.next!=None):
            stack.append(slow.data)
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            slow=slow.next
        print(slow.data)
        print(stack)
        while(slow.next!=None):
            if slow.data!=stack[-1]:
                return False
            else:
                slow=slow.next
        return True

if __name__ == '__main__':
    l=LinkedList()
    l.addatbeg(1)
    l.addatbeg(0)
    l.addatbeg(2)
    l.addatbeg(0)
    l.addatbeg(1)
    l.printList()
    print()
    if l.palindrome(l.head):
        print("Yes")
    else:
        print("No")




