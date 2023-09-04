# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nexts=[]
        current=head

        while current:
            if current.next not in nexts:
                nexts.append(current.next)
            else:
                return True
            current=current.next
        
