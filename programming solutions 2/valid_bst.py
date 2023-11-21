# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root,l=float('-inf'),r=float('inf')):
            if not root:
                return True
            
            if l<root.val and root.val<r:
                return bst(root.right,root.val,r) and bst(root.left,l,root.val)
            else:
                return False
        
        return bst(root,float('-inf'),float('inf'))


        
