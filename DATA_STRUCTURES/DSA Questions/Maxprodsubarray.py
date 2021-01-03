def maxm(arr,size):
    max_end=1
    min_end=1
    flag=0
    max_far=0
    for i in range(size):
        if arr[i]>0:
            max_end=max_end*arr[i]
            min_end=min(min_end*arr[i],1)
            flag=1
        elif arr[i]==0:
            max_end=1
            min_end=1
        else:
            temp=max_end
            max_end=max(min_end*arr[i],1)
            min_end=temp*arr[i]
        if max_far<max_end:
            max_far=max_end
    if flag==0 and max_far==0:
        return 0
    return max_far
if __name__ == '__main__':
    arr=[-1, -3, -10, 0, 60]
    s=len(arr)
    m=maxm(arr,s)
    print(m)
