def elements(arr,n,k):
    d=n//k
    freq={}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]]=freq[arr[i]]+1
        else:
            freq[arr[i]]=1
    for i in freq:
        if freq[i]>d:
            print(i)
    print(freq)
if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
    k=4
    elements(arr,len(arr),k)