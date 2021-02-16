class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.hd=0
    def topview(self,root):
        if root==None:
            return
        q=[]
        map=dict()
        hd=0
        root.hd=hd
        q.append(root)
        cont=0
        while(len(q)):
            print(len(q),'Ia am the lenght baby')
            root=q[0]
            hd=root.hd
            if hd not in map:
                map[hd]=root.data
            if root.left:
                root.left.hd=hd-1
                q.append(root.left)
            if root.right:
                root.right.hd=hd+1
                q.append(root.right)
            cont=cont+1
            print(cont,"Inside baby")
            q.pop(0)
            print("I am hd ",hd)
        print(cont,"Val")
        for i in sorted(map):
            print(map[i])
if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(2)
    root.right.left=TreeNode(3)
    root.topview(root)