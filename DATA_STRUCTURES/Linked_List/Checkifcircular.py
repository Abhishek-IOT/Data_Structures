class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None
    def addatend(self,data):
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
if __name__ == '__main__':
    l=LinkedList()
    l.addatend(1)
    l.addatend(2)
    l.addatend(3)
    l.addatend(4)
    l.addatend(5)
    # l.addatend(1)
    l.PrintList()

