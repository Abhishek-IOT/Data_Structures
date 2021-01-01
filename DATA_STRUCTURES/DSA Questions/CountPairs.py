def count(arr,size,sum):
    m=[0]*2*n
    for i in range(0, n):
        m[arr[i]] += 1
    print(m)


arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
count(arr,n,sum)
