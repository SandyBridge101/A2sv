class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head=ListNode(0)
        self.limit=k
        self.size=0
        

    def insertFront(self, value: int) -> bool:
        if self.size<self.limit:
            dummy=ListNode(value)
            queue=self.head.next
            self.head.next=dummy
            self.head.next.next=queue
            self.size+=1
            return True
        else:
            return False


        

    def insertLast(self, value: int) -> bool:
        if self.size<self.limit:
            current=self.head
            while current.next:
                current=current.next
            current.next=ListNode(value)
            self.size+=1
            return True
        else:
            return False

        

    def deleteFront(self) -> bool:
        if self.head.next:
            self.head.next=self.head.next.next
            self.size-=1
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if self.head.next:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=current.next.next
            self.size-=1
            return True
        else:
            return False

        

    def getFront(self) -> int:
        if self.head.next:
            return self.head.next.val
        else:
            return -1
        #return self.head.next.val

        

    def getRear(self) -> int:
        if self.head.next:
            current=self.head
            while current.next:
                current=current.next
            return current.val
        else:
            return -1
            


    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==self.limit
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
