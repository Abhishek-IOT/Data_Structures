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
        min=0
        if self.left:
            min=self.left.inorder_Traversal()
        return min[0]
    def find_max(self):
        maxi=0
        if self.right:
            maxi=self.right.inorder_Traversal()
        return maxi[-1]
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
