def sortstack(stack,element):
    if len(stack)==0 or element>stack[-1]:
        stack.append(element)
        return
    else:
        temp=stack.pop()
        sortstack(stack,element)
        stack.append(temp)
def sorting(stack):
    if len(stack)!=0:
        temp=stack.pop()
        sorting(stack)
        sortstack(stack,temp)
def printingstack(stack):
    for i in stack[::-1]:
        print(i,end=" ")
if __name__ == '__main__':
    s=[]
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
    printingstack(s)
    sorting(s)
    print("After sorting the stack")
    printingstack(s)