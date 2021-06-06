def delmid(s):
    if len(s)==0:
        return -1
    k=(len(s)//2)+1
    print(k)
    solve(s,k)
    return s
def solve(s,k):
    if k==1:
        s.pop()
        return
    temp=s[-1]
    s.pop()
    solve(s,k-1)
    s.append(temp)
    return
s=[1,2,3,4,5,6]
m=delmid(s)
print(m)