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


def heapsort(arr,n):
    start=n//2-1
    for i in range(start,-1,-1):
        heapify(arr,n,i)

if __name__ == '__main__':
    arr1=[10, 5, 6, 2]
    arr2=[12, 7, 9]

    n1=len(arr1)
    n2=len(arr2)
    arr = []
    for i in range(n1):
        arr.append(arr1[i])
    for i in range(n2):
        arr.append(arr2[i])
    print(arr)
    heapsort(arr,len(arr))
    print(arr)