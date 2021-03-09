class Myclass:
    def __init__(self,cap):
        self.capacity=cap
        self.top=-1
        self.l=[]
    def isEmpty(self):
        return True if self.top==-1 else False
    def peek(self):
        return self.l[-1]
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.l.pop()
        else:
            return "$"
    def push(self,element):
        self.top+=1
        self.l.append(element)
    def Evaluate(self,exp):
        for i in exp:
            # print(i)
            if i.isdigit():
                self.push(i)
            else:

                val=self.pop()
                val1=self.pop()
                # print(val1,val)
                # print(i)
                self.push(str(eval(val1+i+val)))
        return int(self.pop())
if __name__ == '__main__':
    exp="231*+9-"
    cap=len(exp)
    o=Myclass(cap)
    m=o.Evaluate(exp)
    print(m)
