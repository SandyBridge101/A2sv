# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        l=1
        while current:
            l+=1
            current=current.next
        mid=ceil(l/2)
        current=head
        x=1
        while current:
            if x==mid:
                break
            x+=1
            current=current.next
        return current
        
