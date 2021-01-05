def threeway(arr,size,low,high):
    start=0
    end=size-1
    i=0
    while i<=end:
        if arr[i]<low:
            temp=arr[i]
            arr[i]=arr[start]
            arr[start]=temp
            i=i+1
            start=start+1
        elif arr[i]>high:
            temp=arr[i]
            arr[i]=arr[end]
            arr[end]=temp
            end=end-1
        else:
            i=i+1
if __name__ == '__main__':
    arr=[1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    threeway(arr,len(arr),14,20)
    print(arr)

