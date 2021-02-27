
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def findlargest(root):
    if root is None:
        return 0
    ans=[-100]
    findlargestutil(root,ans)
    return ans[0]
def findlargestutil(root,ans):
    if root is None:
        return 0
    currsum=root.data+(findlargestutil(root.left,ans)+findlargestutil(root.right,ans))
    ans[0]=max(currsum,ans[0])
    return currsum
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(-2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(-6)
    root.right.right = newNode(2)
    m=findlargest(root)
    print(m)
