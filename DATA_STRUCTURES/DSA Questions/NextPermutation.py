"""

"""
def rev(arr):
    arr=arr[::-1]
    print(arr)
    return arr
def next(arr,n):
    i=n-2

    print(i)
    index=0
    while(i>=0):
        print(arr[i],arr[i+1])
        if arr[i]<arr[i+1]:
            index=i
            break
        i=i-1
    print(index)
    j = n - 1
    while(j>=0):
        print(arr[j],arr[index])
        if arr[j]>arr[index]:
            temp=arr[j]
            arr[j]=arr[index]
            arr[index]=temp
            break
        j=j-1
    print(arr)
    print(index,n-1)
    l=[]
    m=[]
    for j in range(index + 1):
        m.append(arr[j])
    for i in range(index+1,n):
        l.append(arr[i])
    arr1=rev(l)
    m.extend(arr1)
    print(m)
    return m
    # print(arr1)




if __name__ == '__main__':
    arr=[1,2,3]
    #    0 1 2 3 4
    next(arr,len(arr))
    # rev(arr,0,len(arr))