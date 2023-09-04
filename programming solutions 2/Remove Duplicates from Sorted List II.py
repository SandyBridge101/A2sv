class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count={}
        current=head
        while current:
            count[current.val]=1+count.get(current.val,0)
            current=current.next
        print(list(count.keys()))
        dummy=ListNode(0)
        current=dummy
        
        for i in list(count.keys()):
            if count[i]==1:
                current.next=ListNode(i)
                current=current.next
        
        return dummy.next
