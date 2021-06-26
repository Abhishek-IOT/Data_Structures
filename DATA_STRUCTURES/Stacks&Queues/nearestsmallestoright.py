"""
Nearest smallest elememt to the left
arr=[4,5,40,1]
op=[1,1,1,1]
"""
from collections import deque
def nearest(arr,n):
    stack=deque()
    vector=[]
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            vector.append(-1)
        elif len(stack)>0 and stack[-1]<arr[i]:
            vector.append(stack[-1])
        elif len(stack)>0 and stack[-1]>=arr[i]:
            while(len(stack)>0 and stack[-1]>=arr[i]):
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1])
        stack.append(arr[i])
    vector.reverse()
    return vector
if __name__ == '__main__':
    arr=[4,5,40,1]
    op=nearest(arr,len(arr))
    print(op)