class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique=[]
        if not head:return None
        current=head
        while current:
            if current.val not in unique:
                unique.append(current.val)
            current=current.next
        dummy=ListNode(0)
        current=dummy
        current.next=ListNode(0)
        for i in unique:
            current.next=ListNode(i)
            current=current.next

        return dummy.next
