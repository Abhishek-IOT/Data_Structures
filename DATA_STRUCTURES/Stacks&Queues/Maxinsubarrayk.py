from collections import deque
def printMax(arr,n,k):
    queue=deque()
    for i in range(k):
        while(queue and arr[i]>=arr[queue[-1]]):
            # print(arr[i], arr[queue[-1]])
            queue.pop()
        queue.append(i)
    for i in range(k,n):
        print(arr[queue[0]],end=" ")
        while(queue and queue[0]<=i-k):
            queue.popleft()
        while(queue and arr[i]>=arr[queue[-1]]):
            queue.pop()
        queue.append(i)
        # print(queue)
    print(arr[queue[0]])
if __name__ == '__main__':
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    printMax(arr,len(arr),k)
