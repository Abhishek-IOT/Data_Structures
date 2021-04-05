class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,x):
        if ((self.rear)%self.size==self.front):
            print("Queue is Full")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=x
        else:
            self.rear=((self.rear)%self.size)
            self.queue[self.rear]=x
    def dequeue(self):
        if self.front==-1:
            print("Queue is empty")
        elif self.front==self.rear:
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp

