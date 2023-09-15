class RecentCounter:

    def __init__(self):
        self.queue=[]
        self.size=0
        self.front=-1
        self.rear=0

        

    def ping(self, t: int) -> int:
        count=0
        l=t-3000
        r=t
        self.queue.append(t)
        self.size+=1
        #print(self.queue,self.queue[self.front],self.queue[self.rear],l,self.size)

        while self.queue[self.rear]<l:
            self.size-=1
            self.rear+=1
 
        
        return self.size
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
