
def getmin(arr,size):
    m = arr[0]
    index = 0
    for i in range(1, size):
        if arr[i] < m:
            m = arr[i]
            index = i
        if index == size - 1:
            # index = 0
            m=0
    return m,index
def getmax(arr,size,intial):
    m=arr[size-1]
    index=1
    i=size-2
    while(i>intial):
        # print(arr[i],m,i)
        if arr[i]>m:
            m=arr[i]
            index=i
        i=i-1
    return m

def maxprofit(arr,size):
    mini=getmin(arr,size)
    print("The minimum value is ",mini[0],"from index",mini[1])
    maxi=getmax(arr,size,mini[1])
    print(maxi,"the maximum value")
    maxpro=maxi-mini[0]
    if mini[1] == size - 1:
        maxpro = 0
    return maxpro
if __name__ == '__main__':
    arr= [7,6,4,3,1]
    m=maxprofit(arr,len(arr))
    print(m)
    # getmax(arr,len(arr),2)
    # print(y)
