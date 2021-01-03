def maxpro(arr,size):
    pro=0
    for i in range(1,size):
        sub=arr[i]-arr[i-1]
        if sub>0:
            pro=pro+sub
    return pro
if __name__ == '__main__':
    arr=[100, 30, 15, 10, 8, 25, 80]
    m=maxpro(arr,len(arr))
    print(m)
