def push(l,k):
    l.append(k)
    return l
def pop(l,k):
    for i in range(len(l)):
        if l[i]==k:
            l.pop(i)
            return l
    return -1
def isempty(arr):
    if len(arr)<1:
        return True
    else:
        return False
def peek(arr):
    return arr[-1]
if __name__ == '__main__':
    arr=[]
    push(arr,10)
    push(arr,0)
    push(arr,45)
    push(arr,7)
    print(arr)
    m=pop(arr,100)
    print(m)
    t=peek(arr)
    print(t,"It is peek")
    print(arr)
    pop(arr,0)
    pop(arr,10)
    pop(arr,45)
    pop(arr,7)
    if isempty(arr):
        print("YES it is empty")
    else:
        print("NO it is not")
    print(arr)
    print(len(arr))