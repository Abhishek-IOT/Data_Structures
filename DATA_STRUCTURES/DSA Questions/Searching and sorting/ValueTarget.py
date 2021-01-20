def target(arr,value,left,right):
    if right>=left:
        mid=1+(right-left)//2
        if arr[mid]==value:
            return mid
        if arr[mid]>value:
            target(arr,value,mid-1,right)
        else:
            target(arr,value,left,mid+1)
    return -1
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    t=target(arr,x,0,len(arr))
    if t==-1:
        print("not found")
    else:
        print("Yes found it baby at index",t)
