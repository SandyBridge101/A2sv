# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse_sum(root,sum):
            if not root:
                return 
            sum+=root.val

            if not root.left and not root.right:
                if sum==targetSum:
                    return True
                else:
                    return False
            return traverse_sum(root.right,sum) or traverse_sum(root.left,sum)
        if not root:
            return False
        return traverse_sum(root,0)
