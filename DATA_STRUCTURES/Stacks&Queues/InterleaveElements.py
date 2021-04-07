from queue import Queue
def interleave(queue):
    if queue.qsize()%2!=0:
        print("You should have the even number of inputs")
    stack=[]
    half=int(queue.qsize()/2)
    for i in range(half):
        stack.append(queue.queue[0])
        queue.get()
    while(len(stack)!=0):
        queue.put(stack[-1])
        stack.pop()
    for i in range(half):
        queue.put(queue.queue[0])
        queue.get()
    for i in range(half):
        stack.append(queue.queue[0])
        queue.get()
    while(len(stack)!=0):
        queue.put(stack[-1])
        stack.pop()
        queue.put(queue.queue[0])
        queue.get()
if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    interleave(q)
    length = q.qsize()
    for i in range(length):
        print(q.queue[0], end=" ")
        q.get()