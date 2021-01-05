def maxwater(arr,size):
    res = 0
    for i in range(1,size-1):

        left=arr[i]
        for j in range(i):
            print(left, arr[j], "The max in left", max(left, arr[j]))
            left=max(left,arr[j])

        right=arr[i]
        for j in range(i+1,size):
            print(right, arr[j], "The max in right", max(right, arr[j]))
            right=max(right,arr[j])

        res=res+(min(right,left)-arr[i])
        print(res,"the res yo")
    return res
if __name__ == '__main__':
    arr=[3, 0, 2, 0, 4]
    m=maxwater(arr,len(arr))
    print(m)
