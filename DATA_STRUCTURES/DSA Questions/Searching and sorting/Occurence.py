def searchOccur(arr,digit):
    index=0
    for i in range(len(arr)):
        print(arr[i],digit)
        if arr[i]==digit:
            index=i
            break
    last=0
    i=len(arr)-1
    while(i>=0):
        if arr[i]==digit:
            last=i
            break
        i=i-1
    return index,last
if __name__ == '__main__':
    arr=[1 ,3 ,5, 5, 5, 5, 67, 123, 125]
    li=searchOccur(arr,5)
    # print(li)
    print("the first occur",li[0])
    print("The last occur",li[1])

