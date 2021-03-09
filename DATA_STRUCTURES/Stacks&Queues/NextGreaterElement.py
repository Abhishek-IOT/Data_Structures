def createStack():
    s=[]
    return s
def isEmpty(s):
    return len(s)==0
def push(s,x):
    s.append(x)
    return s
def pop(s):
    if isEmpty(s):
        print("No element")
    else:
        return s.pop()
def isgreater(arr):
    s=createStack()
    next=0
    element=0
    push(s,arr[0])
    for i in range(1,len(arr)):
        next=arr[i]
        if isEmpty(s)==False:
            element=pop(s)
            while(element<next):
                print(str(element),"-->",str(next))
                if isEmpty(s)==True:
                    break
                element=pop(s)
            if element>next:
                push(s,element)
        push(s,next)
    while(isEmpty(s)==False):
        element=pop(s)
        next=-1
        print(str(element),"-->",str(next))

arr=[11,13,21,3]
isgreater(arr)