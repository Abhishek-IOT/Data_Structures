def checkpossible(arr,n):
    s=sum(arr)
    if s%2==0:
        return True
    else:
        return False
def solveutil(arr,cur,l,s):
    print("Ua the starin",s)
    if s<0:
        return
    if s==0:
        return True
    for i in range(cur,len(arr)):
        print(s)
        s=s-arr[i]
        l.append(arr[i])
        if solveutil(arr,i+1,l,s)==True:
            return True
        s = s + arr[i]
        l.remove(arr[i])
        print(s,'b')
    return False

def solve(arr,n):
    l=[]
    s=sum(arr)//2
    if checkpossible(arr,len(arr)):
        if solveutil(arr,0,l,s)==True:
            print(l)
            return True
    return False
if __name__ == '__main__':
    arr=[5,5,5,10,5,4,6]
    if solve(arr,len(arr)):
        print("YEs")
    else:
        print("No")