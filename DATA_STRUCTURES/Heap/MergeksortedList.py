class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addNode(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newNode
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
    def toarray(self,arr):
        temp=self.head
        while(temp):
            arr.append(temp.data)
            temp=temp.next
        return arr

if __name__ == '__main__':
    l=LinkedList()
    l.addNode(1)
    l.addNode(2)
    l.addNode(3)
    l.addNode(10)
    l.printList()
    print()
    m=LinkedList()
    m.addNode(18)
    m.addNode(17)
    m.addNode(19)
    m.printList()
    li=[]
    first=m.toarray(li)
    l.toarray(li)
    print()
    print(first)
    first.sort()
    print(first)
    newList=LinkedList()
    for i in range(len(first)):
        newList.addNode(first[i])
    newList.printList()



