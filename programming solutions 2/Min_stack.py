class ListNode:
    def __int__(self,val):
        self.val=val
        self.next=None

class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[2**31]

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<=self.min_stack[-1]:
            self.min_stack.append(val)
        print(self.min_stack)


    def pop(self) -> None:
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
