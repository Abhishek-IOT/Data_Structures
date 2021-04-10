def heapify(arr,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[smallest]>arr[l]:
        smallest=l
    if r<n and arr[smallest]>arr[r]:
        smallest>r
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i],
        heapify(arr,n,smallest)
def buildheap(arr,n):
    start=n//2-1
    for i in range(start,-1,-1):
        heapify(arr,n,i)
def printHeap(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
if __name__ == '__main__':
    arr = [1, 3, 5, 4, 6, 13,
           10, 9, 8, 15, 17];

    n = len(arr)
    buildheap(arr,n)
    printHeap(arr,n)
