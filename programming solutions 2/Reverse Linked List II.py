# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current=head
        arr=[]
        while current:
            arr.append(current.val)
            current=current.next
        
        arr[left-1:right]=arr[left-1:right][::-1]
        x=0
        print(arr)
        current=head

        while current:
            current.val=arr[x]
            x+=1
            current=current.next


        return head
