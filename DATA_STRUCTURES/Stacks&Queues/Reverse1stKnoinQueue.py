from queue import Queue
def reversefirstK(queue,k):
    stack=[]
    count=0
    while(not queue.empty()):
        if count==k:
            print(count)
            break
        else:
            data=queue.queue[0]
            print(data,"I ,a sjsj")
            stack.append(data)
            queue.get()
            count+=1
    print(stack,"I am stack")
    for i in range(len(stack)):
        queue.put(stack[-1])
        stack.pop()
    for i in range(queue.qsize()-k):
        queue.put(queue.queue[0])
        queue.get()
def printQueue(queue):
    while(not queue.empty()):
        data=queue.queue[0]
        print(data,end=" ")
        queue.get()
if __name__ == '__main__':
    queue=Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    queue.put(5)
    reversefirstK(queue,3)
    printQueue(queue)


