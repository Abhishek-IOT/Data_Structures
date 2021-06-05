def sort(arr):
    if len(arr)==1:
        return
    temp=arr[-1]
    arr.pop()
    sort(arr)
    insert(arr,temp)
def insert(arr,temp):
    if len(arr)==0 or arr[len(arr)-1]<=temp:
        arr.append(temp)
        return
    val=arr[-1]
    arr.pop()
    insert(arr,temp)
    arr.append(val)
arr=[2,0,5,1,6,87,4]
sort(arr)
print(arr)