# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}

        def dp(root):
            if not root:
                return 0

            if not root.left and not root.right:
                return root.val

            if root in memo:
                return memo[root]


            r,l=0,0
            rl,rr,lr,ll=0,0,0,0
            if root.right:
                r=dp(root.right)
                if root.right.left:
                    rl=dp(root.right.left)
                if root.right.right:
                    rr=dp(root.right.right)
                

            if root.left:
                l=dp(root.left)
                if root.left.right:
                    lr=dp(root.left.right)
                if root.left.left:
                    ll=dp(root.left.left)


            if root not in memo:
                memo[root]=max(root.val+lr+ll+rl+rr,l+r)
            return memo[root]
            

        return max(dp(root.left)+dp(root.right),dp(root))
