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
    def deleting_the_StaringNode(self):
        "This function will delete the staring node of the Linked List"
        self.start=self.start.next
    def deleting_from_the_value(self,data):
        "This function will delete by taking the value"
        last=self.start
        while(last):
            if(last.value==data):
                break
            previous_node=last
            last=last.next
        previous_node.next=last.next
    def delete_theLastNode(self):
        "This function is for deleting the last ndode of the linked list"
        last=self.start
        while(last.next):
            if last==None:
                break
            previous_Node=last
            last=last.next
            last
        previous_Node.next=None

    def Searching(self,data):
        last=self.start
        while(last!=None):
            if(last.value==data):
                return True

            last=last.next
            return False
    """
    I Will be using merge sort for sorting the Linked List as it is one of the best way for sorting linkedLIST.
    """
    def Merge_The_Sorted(self,left,right):
        "This function for merging the sorted Linked list as It uses the Divide and conquer Technique"
        if left==None:
            return right
        if right==None:
            return left
        if left.data<=right.data:
            result=left
            result.next=self.Merge_The_Sorted(left.next,right)
        else:
            result=right
            result.next=self.Merge_The_Sorted(left,right.next)
    def MergeSort(self,startNode):
        if(startNode==None or startNode.next==None):
            return startNode
        middle=self.GetMiddle(startNode)
        nexttomiddle=middle.next
        left=self.MergeSort(startNode)
        right=self.MergeSort(nexttomiddle)
        sortedList=self.Merge_The_Sorted(left,right)
        return sortedList






    def GetMiddle(self,startNode):
        if(startNode==None):
            return startNode
        slow=startNode
        fast=startNode
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
    def ListPriny(self,start):
        if start is None:
            return
        curr=start
        while(curr):
            print(curr.data)
            curr=curr.next
        print(' ')




if __name__ == '__main__':
    link=LinkedList()
    link.insert_Node_atTheBeginning(10)
    link.insert_Node_atTheBeginning(50)
    link.insert_Node_atTheBeginning(70)
    link.insert_Node_atTheBeginning(20)
    link.insert_Node_atTheBeginning(100)
    link.insert_Node_atTheBeginning(55)
    link.insert_Node_atTheBeginning(60)




