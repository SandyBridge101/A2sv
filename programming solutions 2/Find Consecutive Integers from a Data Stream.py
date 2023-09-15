class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.size=0
        self.count=0
        self.queue=[]
        

    def consec(self, num: int) -> bool:
        self.queue.insert(0,num)
        if num==self.value:
            self.count+=1
        else:
            self.count=0
        self.size+=1

        if self.size>=self.k:
            if self.count>=self.k:
                return True
            else:
                return False

        else:
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
