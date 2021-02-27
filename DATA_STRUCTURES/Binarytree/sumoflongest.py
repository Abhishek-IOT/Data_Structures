import sys
class getNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sumoflongutil(root,sum,len,maxlen,maxsum):
    if root is None:
        if maxlen[0]<len:
            maxlen[0]=len
            maxsum[0]=sum
        elif maxlen[0]==len and maxsum[0]<sum:
            maxsum[0]=sum
        return
    sumoflongutil(root.left,sum+root.data,len+1,maxlen,maxsum)
    sumoflongutil(root.right,sum+root.data,len+1,maxlen,maxsum)

def sumoflong(root):
    if root is None:
        return 0
    maxlen=[0]
    maxsum=[-100]
    sumoflongutil(root,0,0,maxlen,maxsum)

    return maxsum[0]
if __name__ == '__main__':
    root = getNode(4)  # 4
    root.left = getNode(2)  # / \
    root.right = getNode(5)  # 2 5
    root.left.left = getNode(7)  # / \ / \
    root.left.right = getNode(1)  # 7 1 2 3
    root.right.left = getNode(2)  # /
    root.right.right = getNode(3)  # 6
    root.left.right.left = getNode(6)
    m=sumoflong(root)
    print(m)