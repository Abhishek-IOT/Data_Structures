def makemin(arr,n):
    s1=0
    s2=0
    for i in range(len(arr)-1):
        if len(arr)==2:
            break
        arr.sort()
        s1=s1+arr[0]+arr[1]
        s2=arr[0]+arr[1]
        # print("S1=",s1)
        # print("S2",s2)
        arr.remove(arr[0])
        arr.remove(arr[0])
        arr.append(s2)
    s1=s1+sum(arr)
    return s1
if __name__ == '__main__':
    arr=[4,2,7,6,9]
    m=makemin(arr,len(arr))
    print(m)