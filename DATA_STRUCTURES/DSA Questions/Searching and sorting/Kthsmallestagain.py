def ksmall(arr,k):
    return arr[k-1]
if __name__ == '__main__':
    A=int(input())
    B=int(input())
    l=[]
    for i in range(A,B+1):
       l.append(i)
    print(l)
    k=int(input())
    m=ksmall(l,k)
    print(m)