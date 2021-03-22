def maxValue(s):
    n=len(s)
    stack=[]
    stack.append(-1)
    res=0
    for i in range(n):
        if s[i]=='(':
            stack.append(i)
        else:
            if len(stack)!=0:
                stack.pop()
            if len(stack)!=0:
                res=max(res,i-stack[len(stack)-1])
            else:
                stack.append(i)
    return res
if __name__ == '__main__':
    string = "((()()"

    # Function call
    print(maxValue(string))