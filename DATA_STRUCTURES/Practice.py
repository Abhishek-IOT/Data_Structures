def bruteforce(arr):
    m=[]
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s=s+arr[j]
            m.append(s)
    return m
if __name__ == '__main__':
    arr=[-1,-2,3,4,5]
    n=len(arr)
    m=bruteforce(arr)
    print(m)
    print(max(m))

