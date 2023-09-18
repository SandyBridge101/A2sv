class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.top1=-1
        self.stack2=[]
        self.top2=-1
        self.size=0

        
    def push1(self,x):
        self.top1+=1
        self.stack1[self.top1]=x

    def push2(self,x):
        self.top2+=1
        self.stack2[self.top2]=x

    def pop1(self):
        value=self.stack1[self.top1]
        self.top1-=1
        return value
    
    def pop2(self):
        value=self.stack2[self.top2]
        self.top2-=1
        return value


    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size+=1

    def pop(self) -> int:
        for i in range(self.size-1):
            value=self.stack1.pop()
            print('pops...',value)
            self.stack2.append(value)
        val=self.stack1.pop()
        print('finally pops...',val)
        self.size-=1

        for i in range(self.size):
            value=self.stack2.pop()
            self.stack1.append(value)

        return val

    def peek(self) -> int:
        for i in range(self.size):
            value=self.stack1.pop()
            #print('pops...',value)
            self.stack2.append(value)
        #print(self.stack2[-1])
        val=self.stack2[-1]
        for i in range(self.size):
            value=self.stack2.pop()
            self.stack1.append(value)
        return val
        

    def empty(self) -> bool:
        return self.size==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
