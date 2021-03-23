def redundant(exp):
    stack=[]
    for i in range(len(exp)):
        print(stack)
        if exp[i]=='(' or exp[i]=='+' or exp[i]=='-' or exp[i]=='*'or exp[i]=='/':
            stack.append(exp[i])
        elif exp[i]== ')':
            if stack.pop()=='(':
                return True
            stack.pop()
    return False
exp="((a)+b)"
m=redundant(exp)
print(m)
if m:
    print("Redundant")
else:
    print("Non Redundant")
