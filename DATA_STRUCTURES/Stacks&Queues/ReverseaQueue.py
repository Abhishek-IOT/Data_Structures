from queue import Queue
def PrintQueue(queue):
    while(not queue.empty()):
        print(queue.queue[0],end=" ")
        queue.get()

def reverseaQueue(q):
    stack=[]
    while(not q.empty()):
        stack.append(q.queue[0])
        q.get()
    while(len(stack)!=0):
        q.put(stack[-1])
        stack.pop()
if __name__ == '__main__':
    queue=Queue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    queue.put(40)
    queue.put(50)
    queue.put(60)
    queue.put(70)
    queue.put(80)
    queue.put(90)
    reverseaQueue(queue)
    PrintQueue(queue)
