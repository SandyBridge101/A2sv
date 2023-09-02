# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x=1
        l=0
        if not head.next:
            head=None
            return head
        current=head
        while current:
            l+=1
            current=current.next
        current=head
        if n==l:
            head=head.next
        while current:
            if l-1==n:
                current.next=current.next.next
            current=current.next
            l-=1
        return head
