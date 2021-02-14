def ceilSearch(arr,low,high,x):
    if low>high:
        return -1
    if x<arr[low]:
        return low
    mid=low+(high-low)//2
    if x==arr[mid]:
        return mid
  
if __name__ == '__main__':
    arr=[1,2,3,4,7,10]
    x=5
    m=ceilSearch(arr,0,len(arr)-1,x)
    print(arr[m])

