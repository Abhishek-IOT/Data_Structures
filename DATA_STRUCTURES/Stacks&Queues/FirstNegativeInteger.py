from collections import deque
def printFirstNegative(arr,n,k):
    d=deque()
    for i in range(k):
        if arr[i]<0:
            d.append(i)
    for i in range(k,n):
        if not d:
            print(0)
        else:
            print(arr[d[0]])
        while(d and d[0]<=(i-k)):
            d.popleft()
        if arr[i]<0:
            d.append(i)
    if not d:
        print(0)
    else:
        print(arr[d[0]])
if __name__ == '__main__':
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    n = len(arr)
    k = 3
    printFirstNegative(arr,n,k)