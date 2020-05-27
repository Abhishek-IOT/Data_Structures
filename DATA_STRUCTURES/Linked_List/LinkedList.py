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

