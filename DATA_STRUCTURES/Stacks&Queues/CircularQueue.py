class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,x):
        if ((self.rear+1)%self.size==self.front):
            print("Queue is Full")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=x
        else:
            self.rear=((self.rear+1)%self.size)
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
    def display(self):
        if self.front==-1:
            print("Queue is Empty")
        elif self.rear>=self.front:
            print("Elements in the Queue")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
                print()
        else:
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print("Queue"
                      "")
                print(self.queue[i],end=" ")
                print()
        if (self.rear+1)%self.size==self.front:
            print("Queue is full")
    def length(self):
        return self.size
if __name__ == '__main__':
    queue=CircularQueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    # print(queue.length())
    queue.dequeue()
    queue.display()
    print(queue.length(),"The length of the queue")

