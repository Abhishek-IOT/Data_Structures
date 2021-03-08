class Queue:
    def __init__(self,cap):
        self.front=0
        self.size=0
        self.rear=-1
        self.queue=[None]*cap
        self.capacity=cap
    def isfull(self):
        if self.size==self.capacity:
            return True
        else:
            return False
    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False
    def enqueue(self,item):
        if self.isfull():
            print("Full")
            return
        self.rear=(self.rear+1)%(self.capacity)
        self.queue[self.rear]=item
        self.size+=1
    def dequeue(self,item):
        if self.isEmpty():
            print("Empty")
            return
        self.front=(self.front+1)%(self.capacity)
        self.queue[self.front]=item
        self.size=-1
    def printfront(self):
        if self.isEmpty():
            print("Queue is empty")
        print(self.queue[self.front])
    def printRear(self):
        if self.isEmpty():
            print("Queue is empty")
        print(self.queue[self.rear])
if __name__ == '__main__':
    q=Queue(10)
    q.enqueue(15)
    q.enqueue(1)
    q.enqueue(5)
    q.enqueue(150)
    q.enqueue(153)
    q.printfront()
    q.printRear()