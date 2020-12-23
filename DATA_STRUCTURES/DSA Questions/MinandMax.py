"""
This is the question for finding the minimum and maximum of the array with minimum no of Comparisons
"""
class pair:
    def __init__(self):
        self.min=0
        self.max=0
def getMinMax(arr,n,k):
    minmax=pair()
    if n==1:
        minmax.max=arr[0]
        minmax.min=arr[0]
    if arr[0]>arr[1]:
        minmax.min=arr[1]
        minmax.max=arr[0]
    else:
        minmax.min=arr[0]
        minmax.max=arr[1]
    for i in range(2,n):
        if arr[i]>minmax.max:
            minmax.max=arr[i]
        elif arr[i]<minmax.min:
            minmax.min=arr[i]
    return minmax

if __name__ == '__main__':
    arr=[]
    n=int(input())
    for i in range(n+1):
        arr.append(input())
    maxmin=getMinMax(arr,n,2)
    print("The minimum element",maxmin.min)
    print("The maximum element",maxmin.max)

