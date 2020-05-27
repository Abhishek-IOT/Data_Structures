from DATA_STRUCTURES.Linked_List.Node import Node


class LinkedList:
    def __int__(self):
        self.start=None
    def insert_Node_atTheBeginning(self,data):
        "this function will insert the node at the beginning"
        newnode=Node(data)
        newnode.next=self.start
        #the next node of the new node is start node....so that new node can be added.
        self.start=newnode
    def insert_atTheGivenNode(self,prev_Node,data):
        "this function will help us to add the node at the particular postion"
        if prev_Node is None:
            print("this the beginning")
            return
        newNode=Node(data)
        newNode.next=prev_Node.next
        #Making the new node and making the previous node next as new node next
        prev_Node.next=newNode
        #Hence making the previous node next as newNode


