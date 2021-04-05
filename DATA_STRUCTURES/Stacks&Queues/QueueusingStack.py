class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        while(len(self.s1)!=0):
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while(len(self.s2)!=0):
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def dequeue(self):
        if len(self.s1)==0:
            print("The queue is Empty")
        x=self.s1[-1]
        self.s1.pop()
        return x
    def length(self):
        return len(self.s1)
if __name__ == '__main__':
    q=Queue()
    q.enqueue(1)
    q.enqueue(13)
    q.enqueue(2)
    print("Length",q.length())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("Length" , q.length())

