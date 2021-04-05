from queue import Queue
def stackPermutation(inp,out,n):
    input=Queue()
    output=Queue()
    for i in range(n):
        input.put(inp[i])
    for i in range(n):
        output.put(out[i])
    temp=[]
    while(not input.empty()):
        ele=input.queue[0]
        input.get()
        if ele==output.queue[0]:
            output.get()
            while(len(temp)!=0):
                if temp[-1]==output.queue[0]:
                    temp.pop()
                    output.get()
        else:
            temp.append(ele)
    return len(temp)==0 and input.empty()
if __name__ == '__main__':
    input=[1,2,3]
    output=[3,1,2]
    m=stackPermutation(input,output,2)
    if m==True:
        print("Yes")
    else:
        print("no")
