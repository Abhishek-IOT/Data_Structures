def minswaps(arr,n):
    ans=0
    temp=arr.copy()
    temp.sort()
    for i in range(n):
        if arr[i]!=temp[i]:
            ans=ans+1
            swap(arr,i,index(arr,temp[i]))
    return ans
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def index(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
    return -1



if __name__ == '__main__':
    arr=[4,3,2,1]
    m=minswaps(arr,len(arr))
    print(m)