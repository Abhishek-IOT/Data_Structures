class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def addchild(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right=BinarySearchTree(data)
    def search(self,val):
        if val==self.data:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def inorder_Traversal(self):
        e=[]
        if self.left:
            e+=self.left.inorder_Traversal()
        e.append(self.data)
        if self.right:
            e+=self.right.inorder_Traversal()
        return e
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
       if self.right is None:
           return self.data
       return self.right.find_max()
    def preorder(self):
        e=[]
        e.append(self.data)
        if self.left:
            e+=self.left.preorder()
        if self.right:
            e+=self.right.preorder()
        return e
    def postorder(self):
        e=[]
        if self.left:
           e+=self.left.postorder()
        if self.right:
            e+=self.right.postorder()
        e.append(self.data)
        return e
    def sumofall(self):
        leftsum=0
        rightsum=0
        if self.left:
            leftsum=self.left.sumofall()
        else:
            leftsum=0
        if self.right:
            rightsum=self.right.sumofall()
        else:
            rightsum=0
        return leftsum+rightsum+self.data
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            m=self.left.find_max()
            self.data=m
            self.left=self.left.delete(m)
        return self
    def getlevelutil(self0,self,data,level):
        if self==None:
            return 0
        if self.data==data:
            return level
        down=self.getlevelutil(self.left,data,level+1)
        if down!=0:
            return down
        down=self.getlevelutil(self.right,data,level+1)
        return down
    def getlevel(self,data):
        return self.getlevelutil(self,data,1)
def build_tree(element):
    root=BinarySearchTree(element[0])
    for i in range(1,len(element)):
        root.addchild(element[i])
    return root
if __name__ == '__main__':
    n=[17,4,1,20,9,23,99,18,34]
    print(sum(n))
    tre=build_tree(n)
    print(tre.inorder_Traversal())
    m=tre.search(9)
    print(m)
    minval=tre.find_min()
    print(minval)
    maxval=tre.find_max()
    print(maxval)
    print(tre.preorder())
    print(tre.postorder())
    print(tre.sumofall())
    tre.delete(9)
    tre.delete(17)
    print(tre.inorder_Traversal())
    print(tre.getlevel(1))
    print(tre.getlevel(17))