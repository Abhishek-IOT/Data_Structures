"""Nearest Largest Number to right
IP=[4, 5, 2, 25]
OP=[5,25,25,-1]
"""
from collections import deque
def nearest(arr,n):
    vector=[]
    stack=deque()
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            vector.append(-1)
        elif len(stack)>0 and stack[-1]>arr[i]:
            vector.append(stack[-1])
        elif len(stack)>0 and stack[-1]<arr[i]:
            while(len(stack)>0 and stack[-1]<arr[-1]):
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1])
        stack.append(arr[i])
    vector.reverse()
    return vector
if __name__ == '__main__':
    ip=[4, 5, 2, 25]
    op=nearest(ip,len(ip))
    print(op)
