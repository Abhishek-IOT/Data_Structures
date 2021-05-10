def sumofall(arr,n):
    arr.sort()
    s=0
    for i in range(len(arr)):
        s+=arr[i]*i
    print(s)
if __name__=='__main__':
    arr=[3, 5, 6, 1]
    sumofall(arr,len(arr))
