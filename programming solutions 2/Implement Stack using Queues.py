class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


class MyStack:

    def __init__(self):
        self.stack=ListNode(0)

    def push(self, x: int) -> None:
        current=self.stack
        while current.next:
            current=current.next
        new_node=ListNode(x)
        current.next=new_node

    def pop(self) -> int:
        current=self.stack
        while current:
            if current.next.next==None:
                value=current.next.val
                current.next=None
                break
            current=current.next
        return value
        

    def top(self) -> int:
        current=self.stack
        while current.next:
            current=current.next  
        return current.val

    def empty(self) -> bool:
        if not self.stack.next:
            return  True
             


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
