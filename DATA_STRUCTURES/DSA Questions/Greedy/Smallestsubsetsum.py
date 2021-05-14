def smallestsubset(arr,n):
    sumofelement=sum(arr)
    arr.sort(reverse=True)
    halfsum=sumofelement//2
    currsum=0
    res=0
    print(halfsum)
    for i in range(n):
        currsum=currsum+arr[i]
        res+=1
        if currsum>halfsum:
            return res
    return res
if __name__ == '__main__':
    arr=[2,1,2]
    print(smallestsubset(arr,len(arr)))
