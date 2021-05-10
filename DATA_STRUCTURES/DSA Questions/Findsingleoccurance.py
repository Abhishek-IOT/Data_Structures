def singleoccur(arr):
    d={}
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    return d
if __name__=='__main__':
    arr=[3,4,4,5,5]
    m=singleoccur(arr)
    for i in m:
        if m[i]!=2:
            print(i)
