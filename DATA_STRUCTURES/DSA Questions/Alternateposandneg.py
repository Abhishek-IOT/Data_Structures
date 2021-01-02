def quicksort(arr,low,high):
    if low<high:
        pi=part(arr,low,high)
        print(pi)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
def part(arr,low,high):
    i=low-1
    pivot=arr[high-1]
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    t=arr[i+1]
    arr[i+1]=arr[high-1]
    arr[high-1]=t
    return i+1
def rearrange(arr):
    quicksort(arr,0,len(arr)-1)
    print(arr)
    negative_index=0
    print(arr[negative_index],"nega")
    for j in range(len(arr)):
        if arr[j]>0:
            postive_index=j
            break
    print(postive_index)
    while(negative_index!=postive_index):
        temp=arr[negative_index]
        arr[negative_index]=arr[postive_index]
        arr[postive_index]=temp
        negative_index=negative_index+2
        postive_index=postive_index+1
    print(arr)
if __name__ == '__main__':
    arr = [1, 2, 3, -4, -1, 4]
    n = len(arr)
    rearrange(arr)