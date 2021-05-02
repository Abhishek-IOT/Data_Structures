def minimumcost(n,k,candy):
    if k==n-1:
        return min(candy)
    candy.sort()
    s=0
    for i in range(n-k):
        s=s+candy[i]
    return s
def maximumcost(n,k,candy):
    if k==n-1:
        return max(candy)
    candy.sort()
    candy.reverse()
    s=0
    # print(candy)
    for j in range(n-k):
        s=s+candy[j]
    return s

if __name__ == '__main__':
    candy=[3,2,1,4,5]
    n=5
    k=4
    m=minimumcost(n,k,candy)
    print(m)
    p=maximumcost(n,k,candy)
    print(p)