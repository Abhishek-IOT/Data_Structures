def createStack():
    stack=[]
    return stack
def push(stack,item):
    stack.append(item)
def isEmpty(stack):
    return len(stack)==0
def pop(stack):
    if isEmpty(stack):
        print("Stack is empty")
        exit(1)
    return stack.pop()
def insertAtBottom(stack,item):
    if isEmpty(stack):
        push(stack,item)
    else:
        temp=pop(stack)
        insertAtBottom(stack,item)
        push(stack,temp)
def printStack(stack):
    for i in range(len(stack)):
        print(stack[i],end=' ')
def reverse(stack):
    if not isEmpty(stack):
        temp=pop(stack)
        reverse(stack)
        insertAtBottom(stack,temp)


if __name__ == '__main__':
    s=createStack()
    insertAtBottom(s,4)
    insertAtBottom(s,3)
    insertAtBottom(s,2)
    insertAtBottom(s,1)
    printStack(s)
    print()
    m=createStack()
    push(m,4)
    push(m,3)
    push(m,2)
    push(m,1)
    printStack(m)
    reverse(m)
    print()
    printStack(m)
