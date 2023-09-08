# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self,head,k,l,x):
        count=0
        if not head:
            return None
        print(x,l-x,'counted ...')
        if l-x<k:
            return head
        prev=None
        nxt=None
        prev_head=head
        current=head
        print(head.val,x)
        while current and count<k:
            print(current.val)
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
            count+=1
            x+=1
        
        if nxt:
            head.next=self.reverse(current,k,l,x)

        return prev

        

    

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current=head
        l=0
        while current:
            current=current.next
            l+=1
        x=0
        head=self.reverse(head,k,l,x)

        return head
