from DATA_STRUCTURES.Linked_List.Node import Node


class LinkedList:
    def __init__(self):
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

    def insert_atTheEnd(self,data):
        "This Function is for inserting at the end of the Linked List"
        newNode=Node(data)
        #Now checking that the Linked list os empty if it is empty then the NewNode will be the starting Node
        if self.start is None:
            self.start=newNode
            return
        #Now if this is not the case then we will have to traverse the whole list
        last_Node=self.start
        while(last_Node.next):
            last_Node=last_Node.next
        #After traversing the node we will update the last Node'next to the new Node
        last_Node.next=newNode

    def Printing_The_LinkedList(self):
        "This function is for printing the Linked list"
        node=self.start
        while(node):
            print(node.value)
            node=node.next
