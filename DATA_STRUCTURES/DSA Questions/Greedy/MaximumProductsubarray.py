def maxProdutcSubset(a,n):
    if n==1:
        return a[0]
    max_neg=-9999999999
    count_neg=0
    count_zero=0
    prod=1
    for i in range(n):
        if a[i]==0:
            count_zero+=1
            continue
        if a[i]<0:
            count_neg+=1
            max_neg=max(max_neg,a[i])
        prod=prod*a[i]
    if count_zero==n:
        return 0
    if count_neg&1:
        if count_neg==1 and count_zero>0 and count_neg+count_zero==n:
            return 0
        prod=int(prod/max_neg)
    return prod
if __name__ == '__main__':
    a = [ -1, -1, -2, 4, 3 ]
    n = len(a)
    print(maxProdutcSubset(a, n))