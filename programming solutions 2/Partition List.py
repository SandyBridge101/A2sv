class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=ListNode(0)
        dummy2=ListNode(0)
        small=dummy1
        large=dummy2

        current=head

        while current:
            if current.val>=x:
                large.next=current
                large=large.next
            else:
                small.next=current
                small=small.next
            current=current.next
        large.next=None
        small.next=dummy2.next
        return dummy1.next
