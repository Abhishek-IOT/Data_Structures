def printnext(arr):
    stack=[]
    stack.append(arr[0])
    for i in range(1,len(arr)):
        if len(stack)==0:
            stack.append(arr[i])
        while(len(stack)!=0 and stack[-1]>arr[i]):
            print(stack[-1],"==>",arr[i])
            stack.pop()
        stack.append(arr[i])
    while(len(stack)!=0):
        print(stack[-1],"==>",-1)
        stack.pop()
if __name__ == '__main__':
    arr=[11,13,21,3]
    printnext(arr)

