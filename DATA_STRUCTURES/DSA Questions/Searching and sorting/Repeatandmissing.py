def repeat(arr):
    d={}
    for i in range(1,len(arr)+1):
        d[i]=0

    print(d)
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]]+=1
    print(d)
    l=[]
    for i in d:
        if d[i]==0:
            l.append(i)
        if d[i]==2:
            l.append(i)
    return l
if __name__ == '__main__':
    arr=[1,2,2]
    miss=repeat(arr)
    print(miss[1],"The missing element")
    print(miss[0],"the repeated element")