class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        current1=list1
        current2=list2
        if not list1:
            return list2
        elif not list2:
            return list1


        while current1 and current2:
            if current1.val>=current2.val:
                curr.next=current2
                current2=current2.next
            else:
                curr.next=current1
                current1=current1.next
            curr=curr.next
        if current1:
            print(1)
            curr.next=current1
        else:
            print(2)
            curr.next=current2
            
        return dummy.next


