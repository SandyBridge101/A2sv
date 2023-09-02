class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=ListNode(0)
        even=ListNode(0)
        current=head
        temp_odd=odd
        temp_even=even
        x=1
        while current:
            if x%2==0:
                temp_even.next=ListNode(current.val)
                temp_even=temp_even.next
            else:
                temp_odd.next=ListNode(current.val)
                temp_odd=temp_odd.next
            x+=1
            current=current.next
            temp_odd.next=even.next
        return odd.next
        
