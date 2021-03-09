def revese(s):
    stack=[]
    for char in s:
        stack.append(char)
    m=""
    for i in range(len(stack)):
        m=m+stack.pop()
    print(m)
if __name__ == '__main__':
    s="GeeksforGeeks"
    revese(s)