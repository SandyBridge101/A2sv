# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        def traverse(root):
            if not root:
                return
            arr.append(root.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        heapq.heapify(arr)
        n=1
        while n<k:
            heapq.heappop(arr)
            n+=1
        return heapq.heappop(arr)
        
