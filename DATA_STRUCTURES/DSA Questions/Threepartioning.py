"""
Three way partitioning of an array around a given range
Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts.
1) All elements smaller than lowVal come first.
2) All elements in range lowVal to highVVal come next.
3) All elements greater than highVVal appear in the end.
The individual elements of three sets can appear in any order
We can simply sort the array and get the ans(but it takes more time) but we will use this logic to make the ans in less time.
We will have to pointer first start and then end and we will check if the arr[i] is greater or lesser than the range and
then set the array accordingly
if the value is less than low push it in start and increment the start
if the value is more then high push at the end and decrement the end

"""

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

