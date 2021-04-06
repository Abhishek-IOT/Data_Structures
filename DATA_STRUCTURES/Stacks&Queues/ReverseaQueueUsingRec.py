from queue import Queue
def reverse(queue):
    if queue.empty():
        return queue
    else:
        data=queue.queue[0]
        queue.get()
        reverse(queue)
        queue.put(data)
def printQueue(queue):
    while(not queue.empty()):
        data=queue.queue[0]
        queue.get()
        print(data,end=" ")
if __name__ == '__main__':
    queue=Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    reverse(queue)
    printQueue(queue)