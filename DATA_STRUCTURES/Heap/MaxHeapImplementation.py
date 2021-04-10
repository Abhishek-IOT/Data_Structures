def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[largest]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i],
        heapify(arr,n,largest)
def buildheap(arr,n):
    start=n//2-1
    for i in range(start,-1,-1):
        heapify(arr,n,i)
def printHeap(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
if __name__ == '__main__':
    arr = [ 1, 3, 5, 4, 6, 13,
             10, 9, 8, 15, 17 ]
    n=len(arr)
    buildheap(arr,n)
    printHeap(arr,n)
